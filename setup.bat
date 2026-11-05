
@echo off
cd /d "%~dp0"

echo Installing NV DayZ Discord Bot...

py -m venv .venv

if errorlevel 1 (
    echo Python installation failed.
    pause
    exit /b 1
)

call .venv\Scripts\activate.bat

python -m pip install --upgrade pip
python -m pip install -r requirements.txt

echo.
echo Setup complete!
pause
