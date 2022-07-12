#!/bin/bash
# Seed builder
# AUTO_GENERATED (Read only)

RUNNING=$(sudo docker compose -f bin/docker/docker-compose.yml ps --services --filter "status=running")
if [ $RUNNING -z ]; then
  echo "ERROR: Before executing bin/dump.sh, start server with bin/start.sh"
  exit 1
fi

MODEL_NAME="None"
FILE_PATH="./dump.yaml"

if [ $# -ge 1 ]; then MODEL_NAME=$1; fi
if [ $# -ge 2 ]; then FILE_PATH=$2; fi

sudo docker compose -f bin/docker/docker-compose.yml exec django /bin/sh -c "python ./bin/scripts/dump.py $MODEL_NAME $FILE_PATH"