#!/bin/bash
# Seed builder
# AUTO_GENERATED (Read only)

RUNNING=$(docker-compose -f bin/docker/docker-compose.dev.yml ps --services --filter "status=running")
if [ $RUNNING -z ]; then
  echo "ERROR: Before executing bin/query.sh, start server with bin/start.sh"
  exit 1
fi

echo "== Opening psql console"
sudo docker-compose -f bin/docker/docker-compose.dev.yml exec django /bin/sh -c "python manage.py dbshell"