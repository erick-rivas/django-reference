#!/bin/bash
# Seed builder
# AUTO_GENERATED (Read only)
# Use $ bin/dump.sh <model_name> <file_path>

RUNNING=$(sudo docker compose ps --services --filter "status=running")
if [ $RUNNING -z ]; then
  echo "ERROR: Before executing bin/dump.sh, start server with bin/start.sh"
  exit 1
fi

MODEL_NAME="None"
FILE_PATH="./dump.yaml"

if [ $# -ge 1 ]; then MODEL_NAME=$1; fi
if [ $# -ge 2 ]; then FILE_PATH=$2; fi

sudo docker compose exec django /bin/sh -c "python ./bin/scripts/dump.py $MODEL_NAME $FILE_PATH"