@echo off
:: Seed builder
:: AUTO_GENERATED (Read only)

set /A MAX_LINES=250
set SCOPE=None
IF NOT "%~1" == "" set /A MAX_LINES=%1
IF NOT "%~2" == "" set SCOPE=%2

IF "%SCOPE%" == "None" (
    docker compose -f bin/docker/docker-compose.yml logs --follow --tail %MAX_LINES% django celery
) ELSE (
    docker compose -f bin/docker/docker-compose.yml logs --follow --tail %MAX_LINES% %SCOPE%
)