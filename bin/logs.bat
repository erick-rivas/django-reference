@echo off
:: Seed builder
:: AUTO_GENERATED (Read only)

set SCOPE=all
set ONLY_LATEST=false
set /A MAX_LINES=250

IF NOT "%~1" == "" set SCOPE=%1
IF NOT "%~2" == "" set ONLY_LATEST=%2
IF NOT "%~3" == "" set /A MAX_LINES=%3

IF "%SCOPE%" == "all" (
    IF "%ONLY_LATEST%" == "true" (
        docker compose -f bin/docker/docker-compose.yml logs --follow --since 0m --tail %MAX_LINES% django celery
    ) ELSE (
        docker compose -f bin/docker/docker-compose.yml logs --follow --tail %MAX_LINES% django celery
    )
) ELSE (
    IF "%ONLY_LATEST%" == "true" (
        docker compose -f bin/docker/docker-compose.yml logs --follow --since 0m --tail %MAX_LINES% %SCOPE%
    ) ELSE (
        docker compose -f bin/docker/docker-compose.yml logs --follow --tail %MAX_LINES% %SCOPE%
    )
)