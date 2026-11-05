
@echo off
cd /d "%~dp0"

echo Starting NV DayZ Player Count Bot...
echo.

.venv\Scripts\python.exe main.py

echo.
echo Bot has stopped.
pause
