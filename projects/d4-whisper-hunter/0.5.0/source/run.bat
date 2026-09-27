@echo off
setlocal
cd /d "%~dp0"
python -m whisper_hunter
if errorlevel 1 pause
