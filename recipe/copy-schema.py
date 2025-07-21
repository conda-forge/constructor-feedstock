from pathlib import Path
import os
import sys

SP_DIR = Path(os.environ["SP_DIR"])
PREFIX = Path(os.environ["PREFIX"])
SRC_DIR = Path(os.environ["SRC_DIR"])
DATA_DIR = SP_DIR / "constructor/data"
SCHEMA_IN_SRC = SRC_DIR / "constructor/data/construct.schema.json"
SCHEMA_IN_SP = DATA_DIR / SCHEMA_IN_SRC.name


def main() -> int:
    """Ensure the schema is deployed."""
    if not SCHEMA_IN_SP.exists():
        print("... copying:", [SCHEMA_IN_SRC, SCHEMA_IN_SP])
        DATA_DIR.mkdir(parents=True, exist_ok=True)
        SCHEMA_IN_SP.write_bytes(SCHEMA_IN_SRC.read_bytes())

    return 0


if __name__ == "__main__":
    sys.exit(main())
