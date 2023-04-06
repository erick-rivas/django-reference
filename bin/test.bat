@echo off
:: Seed builder
:: AUTO_GENERATED (Read only)

for /f "delims=" %%i in ('docker compose -f bin/docker/docker-compose.yml ps --services --filter "status=running"') do set RUNNING=%%i
IF "%RUNNING%" == "" echo ERROR: Before executing bin/test.bat, start server with bin/start.bat
IF "%RUNNING%" == "" exit 1

set /A SUB_PATH=None
IF NOT "%~1" == "" set SUB_PATH=%1

IF "%SUB_PATH%" == "None" (
    echo == Executing all test cases
    docker compose -f bin/docker/docker-compose.yml exec django /bin/sh -c "python manage.py test"
) ELSE (
    echo == Executing /%SUB_PATH% test cases
    docker compose -f bin/docker/docker-compose.yml exec django /bin/sh -c "python manage.py test %SUB_PATH%/ "
)