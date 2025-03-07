@echo off
:: Seed builder
:: AUTO_GENERATED (Read only)

set SCOPE=all
set /A MAX_LINES=250
set ONLY_LATEST=false

IF NOT "%~1" == "" set SCOPE=%1
IF NOT "%~2" == "" set /A MAX_LINES=%2
IF NOT "%~3" == "" set ONLY_LATEST=%3

IF "%SCOPE%" == "all" (
  IF "%ONLY_LATEST%" == "true" (
    docker compose logs --follow --since 0m --tail %MAX_LINES% django celery
  ) ELSE (
    docker compose logs --follow --tail %MAX_LINES% django celery
  )
) ELSE (
  IF "%ONLY_LATEST%" == "true" (
    docker compose logs --follow --since 0m --tail %MAX_LINES% %SCOPE%
  ) ELSE (
    docker compose logs --follow --tail %MAX_LINES% %SCOPE%
  )
)