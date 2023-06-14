#!/bin/bash
# Seed builder
# AUTO_GENERATED (Read only)

MAX_LINES=250
SCOPE="None"
if [ $# -ge 1 ]; then MAX_LINES=$1; fi
if [ $# -ge 2 ]; then SCOPE=$2; fi

if [ $SCOPE = "None" ]; then
  sudo docker compose -f bin/docker/docker-compose.yml logs --follow --tail $MAX_LINES django celery
else
  sudo docker compose -f bin/docker/docker-compose.yml logs --follow --tail $MAX_LINES $SCOPE
fi