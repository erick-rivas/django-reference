#!/bin/bash
# Seed builder
# AUTO_GENERATED (Read only)

echo "== Restarting celery & redis"
sudo docker compose exec celery /bin/sh -c "celery -A seed.app purge"
sudo docker compose exec redis /bin/sh -c "redis-cli flushall"

echo "== Stopping server"
sudo docker compose stop

echo "== Starting server"
source .env
sudo docker compose start
echo ""
echo "== Server is running in background ($SERVER_URL)"
echo "    - To show logs execute bin/logs.sh"
echo "    - To stop server execute bin/stop.sh"
echo ""