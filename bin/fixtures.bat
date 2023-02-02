@echo off
:: Seed builder
:: AUTO_GENERATED (Read only)

for /f "delims=" %%i in ('docker compose -f bin/docker/docker-compose.yml ps --services --filter "status=running"') do set RUNNING=%%i
IF "%RUNNING%" == "" echo ERROR: Before executing bin/fixtures.bat, start server with bin/start.bat
IF "%RUNNING%" == "" exit 1

set /A SUB_PATH=None
IF NOT "%~1" == "" set /A SUB_PATH=%1

echo == Executing fixtures
IF "%SUB_PATH%" == "None" (
    docker compose -f bin/docker/docker-compose.yml exec django /bin/sh -c "python manage.py loaddata models/fixtures/*.yaml"
) ELSE (
    docker compose -f bin/docker/docker-compose.yml exec django /bin/sh -c "python manage.py loaddata models/fixtures/%SUB_PATH%/*.yaml"
)