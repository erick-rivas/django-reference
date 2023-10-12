@echo off
:: Seed builder
:: AUTO_GENERATED (Read only)

echo == Restarting celery & redis
docker compose exec celery /bin/sh -c "celery -A seed.app purge -f"
docker compose exec redis /bin/sh -c "redis-cli flushall"

echo == Stopping server
docker compose stop

echo == Starting server
FOR /F "eol=# tokens=*" %%i IN (.env) DO SET %%i
docker compose start
echo.
echo == Server is running in background (http://localhost:%COMPOSE_DJANGO_PORT%)
echo     - To show logs execute bin/logs.bat
echo     - To stop server execute bin/stop.bat
echo.