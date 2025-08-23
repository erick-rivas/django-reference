@echo off
:: Seed builder
:: AUTO_GENERATED (Read only)
:: Use $ bin/fixtures.bat <sub_path>

for /f "delims=" %%i in ('docker compose ps --services --filter "status=running"') do set RUNNING=%%i
IF "%RUNNING%" == "" (
  echo ERROR: Before executing bin/console.bat, start server with bin/start.bat
  exit 1
)

set SUB_PATH=None
IF NOT "%~1" == "" set SUB_PATH=%1

IF "%SUB_PATH%" == "None" (
  echo == Executing fixtures in models/fixtures/*.yaml
  docker compose exec django /bin/sh -c "python manage.py loaddata models/fixtures/*.yaml"
) ELSE (
  echo == Executing fixtures in models/fixtures/%SUB_PATH%/*.yaml
  docker compose exec django /bin/sh -c "python manage.py loaddata models/fixtures/%SUB_PATH%/*.yaml"
)