@echo off

:: Create virtual environment
python -m venv venv
call venv\Scripts\activate

:: Install package
pip install -e .

:: Install Playwright browsers
playwright install

:: Set up configuration directory
set CONFIG_DIR=%LOCALAPPDATA%\ai-agent
if not exist "%CONFIG_DIR%" mkdir "%CONFIG_DIR%"

:: Copy example files if they don't exist
if not exist "%CONFIG_DIR%\config.json" copy config.json "%CONFIG_DIR%"
if not exist "%CONFIG_DIR%\.env" copy .env.example "%CONFIG_DIR%\.env"

echo Installation complete!
echo Please edit your configuration files in: %CONFIG_DIR%
echo Run with: ai-agent