#!/bin/bash
# Seed builder
# AUTO_GENERATED (Read only)
# Use $ bin/stop.sh

echo "== Stopping server"
sudo docker compose exec celery /bin/sh -c "celery -A seed.app purge -f"
sudo docker compose exec redis /bin/sh -c "redis-cli flushall"
sudo docker compose stop