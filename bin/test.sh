#!/bin/bash
# Seed builder
# AUTO_GENERATED (Read only)

RUNNING=$(sudo docker compose -f bin/docker/docker-compose.yml ps --services --filter "status=running")
if [ $RUNNING -z ]; then
  echo "ERROR: Before executing bin/test.sh, start server with bin/start.sh"
  exit 1
fi

SUB_PATH="None"
if [ $# -ge 1 ]; then SUB_PATH=$1; fi

if [ $SUB_PATH = "None" ]; then
  echo "== Executing all test cases"
  sudo docker compose -f bin/docker/docker-compose.yml exec django /bin/sh -c "python manage.py test"
else
  echo "== Executing /$SUB_PATH test cases"
  sudo docker compose -f bin/docker/docker-compose.yml exec django /bin/sh -c "python manage.py test $SUB_PATH/ "
fi