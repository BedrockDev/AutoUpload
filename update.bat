@echo off
@echo Installing packages...

FOR /F %%i IN (packages.txt) DO @echo. & @echo Installing %%i via pip install & @echo. & pip install %%i

@echo.
REM @pause