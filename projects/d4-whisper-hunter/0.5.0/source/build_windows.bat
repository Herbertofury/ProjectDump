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
  exit /b 1
)
if not exist .venv-build\Scripts\python.exe py -%PYVER% -m venv .venv-build
if errorlevel 1 exit /b 1
call .venv-build\Scripts\activate.bat
python -m pip install --upgrade pip
python -m pip install -r requirements-build.txt
if errorlevel 1 exit /b 1
python scripts\fetch_upstream_map.py
if errorlevel 1 exit /b 1
python -m compileall -q whisper_hunter d4_whisper_hunter.py tests
if errorlevel 1 exit /b 1
python -m pytest -q
if errorlevel 1 exit /b 1
pyinstaller --noconfirm --clean --onefile --windowed --name "D4WhisperHunter" --collect-all cv2 --add-data "assets\map_5_small.jpg;assets" d4_whisper_hunter.py
if errorlevel 1 exit /b 1
echo Built and tested: dist\D4WhisperHunter.exe
