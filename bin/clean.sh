#!/bin/bash
# Seed builder
# AUTO_GENERATED (Read only)
# Use $ bin/clean.sh <clean_files>

CLEAN_FILES=false

if [ $# -ge 1 ]; then CLEAN_FILES=$1; fi

echo "== Cleaning unused docker resources"
sudo docker image prune --force
sudo docker volume prune --force

if [ "$CLEAN_FILES" = true ]; then
  echo "== Cleaning unused files"
  sudo docker compose exec django /bin/sh -c "python ./bin/scripts/clean_files.py"
fi