#!/bin/bash
# Seed builder
# AUTO_GENERATED (Read only)

RUNNING=$(sudo docker compose ps --services --filter "status=running")
if [ $RUNNING -z ]; then
  echo "ERROR: Before executing bin/debug.sh, start server with bin/start.sh"
  exit 1
fi

sudo docker compose exec django /bin/sh -c "python ./bin/scripts/debug.py"