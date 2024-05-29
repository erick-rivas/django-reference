@echo off
:: Seed builder
:: AUTO_GENERATED (Read only)

for /f "delims=" %%i in ('docker compose ps --services --filter "status=running"') do set RUNNING=%%i
IF "%RUNNING%" == "" echo ERROR: Before executing bin/terminal.bat, start server with bin/start.bat
IF "%RUNNING%" == "" exit 1

set CONTAINER=None
set COMMAND=None
IF NOT "%~1" == "" set CONTAINER=%1
IF NOT "%~2" == "" set CONTAINER=%2

IF "%CONTAINER%" == "celery" (
  echo == Opening %CONTAINER% terminal
  IF "%COMMAND%" == "None" (
    docker compose exec celery /bin/bash
  ) ELSE (
    docker compose exec celery /bin/bash %COMMAND%
  )
) ELSE (
  echo == Opening django terminal
  IF "%COMMAND%" == "None" (
    docker compose exec django /bin/bash
  ) ELSE (
    docker compose exec django /bin/bash %COMMAND%
  )
)