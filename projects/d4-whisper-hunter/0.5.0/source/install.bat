@echo off
setlocal
cd /d "%~dp0"
set "PYVER="
for %%V in (3.14 3.13 3.12 3.11) do (
  if not defined PYVER (
    py -%%V -c "import sys; print(sys.version)" >nul 2>nul
    if not errorlevel 1 set "PYVER=%%V"
  )
)
if not defined PYVER (
  echo Python 3.11-3.14 is required.
  echo Official download: https://www.python.org/downloads/windows/
  pause
  exit /b 1
)
echo Using Python %PYVER%
py -%PYVER% -m venv .venv
if errorlevel 1 exit /b 1
call .venv\Scripts\activate.bat
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
if errorlevel 1 (
  echo Installation failed.
  pause
  exit /b 1
)
echo.
echo Installed. Run D4 Whisper Hunter with run-venv.bat
pause
