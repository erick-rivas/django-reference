@echo off
:: Seed builder
:: AUTO_GENERATED (Read only)

set SCOPE=all
IF NOT "%~1" == "" set SCOPE=%1

echo == Stopping server
IF "%SCOPE%" == "all" (
  echo == Restarting celery & redis
  docker compose exec celery /bin/sh -c "celery -A seed.app purge -f"
  docker compose exec redis /bin/sh -c "redis-cli flushall"
  docker compose stop
) ELSE (
  docker compose stop %SCOPE%
)

echo == Starting server
FOR /F "eol=# tokens=*" %%i IN (.env) DO SET %%i
IF "%SCOPE%" == "all" (
  docker compose start
) ELSE (
  docker compose start %SCOPE%
)
echo.
echo == Server is running in background (http://localhost:%COMPOSE_DJANGO_PORT%)
echo     - To show logs execute bin/logs.bat
echo     - To stop server execute bin/stop.bat
echo.