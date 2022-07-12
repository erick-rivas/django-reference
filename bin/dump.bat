@echo off
:: Seed builder
:: AUTO_GENERATED (Read only)

for /f "delims=" %%i in ('docker compose -f bin/docker/docker-compose.yml ps --services --filter "status=running"') do set RUNNING=%%i
IF "%RUNNING%" == "" echo ERROR: Before executing bin/dump.bat, start server with bin/start.bat
IF "%RUNNING%" == "" exit 1

set MODEL_NAME=None
set FILE_PATH=./dump.yaml

IF NOT "%~1" == "" set MODEL_NAME=%1
IF NOT "%~2" == "" set FILE_PATH=%2

docker compose -f bin/docker/docker-compose.yml exec django /bin/sh -c "python ./bin/scripts/dump.py %MODEL_NAME% %FILE_PATH%"