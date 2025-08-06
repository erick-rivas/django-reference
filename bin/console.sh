#!/bin/bash
# Seed builder
# AUTO_GENERATED (Read only)
# Use $ bin/console.sh <container> <command>

RUNNING=$(sudo docker compose ps --services --filter "status=running")
if [ $RUNNING -z ]; then
  echo "ERROR: Before executing bin/console.sh, start server with bin/start.sh"
  exit 1
fi

CONTAINER="None"
COMMAND="None"
if [ $# -ge 1 ]; then CONTAINER=$1; fi
if [ $# -ge 2 ]; then COMMAND=$2; fi

if [ $CONTAINER = "celery" ]; then
  echo "== Opening $CONTAINER terminal"
  if [ $COMMAND = "None" ]; then
    sudo docker compose exec celery /bin/bash
  else
    sudo docker compose exec celery /bin/bash $COMMAND
  fi
else
  echo "== Opening django terminal"
  if [ $COMMAND = "None" ]; then
    sudo docker compose exec django /bin/bash
  else
    sudo docker compose exec django /bin/bash $COMMAND
  fi
fi