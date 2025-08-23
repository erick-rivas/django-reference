@echo off
:: Seed builder
:: AUTO_GENERATED (Read only)
:: Use $ bin/stop.bat

echo == Stopping server
docker compose exec celery /bin/sh -c "celery -A seed.app purge -f"
docker compose exec redis /bin/sh -c "redis-cli flushall"
docker compose stop