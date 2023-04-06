#!/bin/bash
# Seed builder
# AUTO_GENERATED (Read only)

RUNNING=$(sudo docker compose -f bin/docker/docker-compose.yml ps --services --filter "status=running")
if [ $RUNNING -z ]; then
  echo "ERROR: Before executing bin/fixtures.sh, start server with bin/start.sh"
  exit 1
fi

SUB_PATH="None"
if [ $# -ge 1 ]; then SUB_PATH=$1; fi

if [ $SUB_PATH = "None" ]; then
  echo "== Executing fixtures in models/fixtures/*.yaml"
  sudo docker compose -f bin/docker/docker-compose.yml exec django /bin/sh -c "python manage.py loaddata models/fixtures/*.yaml"
else
  echo "== Executing fixtures in Running models/fixtures/$SUB_PATH/*.yaml"
  sudo docker compose -f bin/docker/docker-compose.yml exec django /bin/sh -c "python manage.py models/fixtures/$SUB_PATH/*.yaml"
fi