@echo off
:: Seed builder
:: AUTO_GENERATED (Read only)

for /f "delims=" %%i in ('docker compose ps --services --filter "status=running"') do set RUNNING=%%i
IF "%RUNNING%" == "" echo ERROR: Before executing bin/terminal.bat, start server with bin/start.bat
IF "%RUNNING%" == "" exit 1

set CONTAINER=None
IF NOT "%~1" == "" set CONTAINER=%1

IF "%CONTAINER%" == "celery" (
  echo == Opening %CONTAINER% terminal
  docker compose exec celery /bin/bash
) ELSE (
  echo == Opening django terminal
  docker compose exec django /bin/bash
)