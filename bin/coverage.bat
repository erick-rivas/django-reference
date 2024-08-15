@echo off
:: Seed builder
:: AUTO_GENERATED (Read only)

for /f "delims=" %%i in ('docker compose ps --services --filter "status=running"') do set RUNNING=%%i
IF "%RUNNING%" == "" echo "ERROR: Before executing bin/coverage.bat, start server with bin/start.bat"
IF "%RUNNING%" == "" exit 1

set SUB_PATH=None
IF NOT "%~1" == "" set SUB_PATH=%1

IF "%SUB_PATH%" == "None" (
  echo == Executing full coverage
  docker compose exec django /bin/sh -c "coverage run --omit='.venv/*,bin/*,tests/*,*__init__*,seed/*, app/*' manage.py test"
) ELSE (
  echo == Executing /%SUB_PATH% coverage
  docker compose exec django /bin/sh -c "coverage run --omit='.venv/*,bin/*,tests/*,*__init__*,seed/*, app/*' manage.py test %SUB_PATH%/ "
)

docker compose exec django /bin/sh -c "coverage report -m"
docker compose exec django /bin/sh -c "coverage xml"