#!/bin/bash
# Seed builder
# AUTO_GENERATED (Read only)

SCOPE="all"
ONLY_LATEST=false
MAX_LINES=250

if [ $# -ge 1 ]; then SCOPE=$1; fi
if [ $# -ge 2 ]; then ONLY_LATEST=$2; fi
if [ $# -ge 3 ]; then MAX_LINES=$3; fi

if [ "$SCOPE" = "all" ]; then
  if [ "$ONLY_LATEST" = true ]; then
    sudo docker compose logs --follow --since 0m --tail "$MAX_LINES" django celery
  else
    sudo docker compose logs --follow --tail "$MAX_LINES" django celery
  fi
else
  if [ "$ONLY_LATEST" = true ]; then
    sudo docker compose logs --follow --since 0m --tail "$MAX_LINES" "$SCOPE"
  else
    sudo docker compose logs --follow --tail "$MAX_LINES" "$SCOPE"
  fi
fi