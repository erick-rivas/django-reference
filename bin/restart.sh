#!/bin/bash
# Seed builder
# AUTO_GENERATED (Read only)

echo "== Restarting celery & redis"
sudo docker compose -f bin/docker/docker-compose.yml exec celery /bin/sh -c "celery -A seed.app purge"
sudo docker compose -f bin/docker/docker-compose.yml exec redis /bin/sh -c "redis-cli flushall"

echo "== Stopping server"
sudo docker compose -f bin/docker/docker-compose.yml stop

echo "== Starting server"
PORT=$(cat bin/docker/.port)
sudo docker compose -f bin/docker/docker-compose.yml start
echo ""
echo "== Server is running in background (http://localhost:$PORT)"
echo "    - To show logs execute bin/logs.sh"
echo "    - To stop server execute bin/stop.sh"
echo ""