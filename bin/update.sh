#!/bin/bash
# Seed builder
# AUTO_GENERATED (Read only)

RUNNING=$(sudo docker-compose -f bin/docker/docker-compose-dev.yml ps --services --filter "status=running")
if [ $RUNNING -z ]; then
  echo "ERROR: Before executing bin/update.sh, start server with bin/start.sh"
  exit 1
fi

echo "== Updating database"
sudo docker-compose -f bin/docker/docker-compose-dev.yml exec django_reference_django /bin/sh -c "bin/docker/db-update.sh"