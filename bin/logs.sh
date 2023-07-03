#!/bin/bash
# Seed builder
# AUTO_GENERATED (Read only)

SCOPE="None"
MAX_LINES=250
if [ $# -ge 1 ]; then SCOPE=$1; fi
if [ $# -ge 2 ]; then MAX_LINES=$2; fi

if [ $SCOPE = "None" ]; then
  sudo docker compose -f bin/docker/docker-compose.yml logs --follow --tail $MAX_LINES django celery
else
  sudo docker compose -f bin/docker/docker-compose.yml logs --follow --tail $MAX_LINES $SCOPE
fi