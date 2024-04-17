#!/bin/bash
# Seed builder
# AUTO_GENERATED (Read only)

RUNNING=$(sudo docker compose ps --services --filter "status=running")
if [ $RUNNING -z ]; then
  echo "ERROR: Before executing bin/terminal.sh, start server with bin/start.sh"
  exit 1
fi

CONTAINER="None"
if [ $# -ge 1 ]; then CONTAINER=$1; fi

if [ $CONTAINER = "celery" ]; then
  echo "== Opening $CONTAINER terminal"
  sudo docker compose exec celery /bin/bash
else
  echo "== Opening django terminal"
  sudo docker compose exec django /bin/bash
fi