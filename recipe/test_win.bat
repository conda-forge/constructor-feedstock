:: setup for signing during tests
set "CONSTRUCTOR_PFX_CERTIFICATE_PASSWORD=1234"
set "CONSTRUCTOR_SIGNING_CERTIFICATE=examples\signing\certificate.pfx"
set "CONSTRUCTOR_SIGNTOOL_PATH=C:\Program Files (x86)\Windows Kits\10\bin\10.0.17763.0\x86\signtool.exe"
powershell scripts\create_self_signed_certificate.ps1 || goto :error

:: run integration tests
python scripts/run_examples.py || goto :error

:error
echo Failed with error #%errorlevel%.
exit 1
