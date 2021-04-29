#!/bin/bash
# Seed builder
# AUTO_GENERATED (Read only)

echo "== Updating database"
RUNNING=$(docker-compose -f bin/docker/docker-compose.dev.yml ps --services --filter "status=running")
if [ $RUNNING -z ]; then
  echo "ERROR: Before executing bin/update.sh, start server with bin/start.sh"
  exit 1
fi
sudo docker-compose -f bin/docker/docker-compose.dev.yml exec django /bin/sh -c "bin/docker/entrypoint.sh"