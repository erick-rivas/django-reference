@echo off
:: Seed builder
:: AUTO_GENERATED (Read only)
:: Use $ bin/dump.bat <model_name> <file_path>

for /f "delims=" %%i in ('docker compose ps --services --filter "status=running"') do set RUNNING=%%i
IF "%RUNNING%" == "" echo ERROR: Before executing bin/dump.bat, start server with bin/start.bat
IF "%RUNNING%" == "" exit 1

set MODEL_NAME=None
set FILE_PATH=./dump.yaml

IF NOT "%~1" == "" set MODEL_NAME=%1
IF NOT "%~2" == "" set FILE_PATH=%2

docker compose exec django /bin/sh -c "python ./bin/scripts/dump.py %MODEL_NAME% %FILE_PATH%"