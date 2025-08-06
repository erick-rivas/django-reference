#!/bin/bash
# Seed builder
# AUTO_GENERATED (Read only)
# Use $ bin/restart.sh <container>

CONTAINER="all"
if [ $# -ge 1 ]; then CONTAINER=$1; fi

echo "== Stopping server"
if [ "$CONTAINER" = "all" ]; then
  echo "== Restarting celery & redis"
  sudo docker compose exec celery /bin/sh -c "celery -A seed.app purge -f"
  sudo docker compose exec redis /bin/sh -c "redis-cli flushall"
  sudo docker compose stop
else
  sudo docker compose stop "$CONTAINER"
fi

echo "== Starting server"
source .env
if [ "$CONTAINER" = "all" ]; then
  sudo docker compose start
else
  sudo docker compose start "$CONTAINER"
fi

echo ""
echo "== Server is running in background (http://localhost:$COMPOSE_DJANGO_PORT)"
echo "    - To show logs execute bin/logs.sh"
echo "    - To stop server execute bin/stop.sh"
echo ""