#!/bin/bash
# Seed builder
# AUTO_GENERATED (Read only)
# Use $ bin/clean.sh <cleaning_type docker|files>

RUNNING=$(sudo docker compose ps --services --filter "status=running")
if [ $RUNNING -z ]; then
  echo "ERROR: Before executing bin/coverage.sh, start server with bin/start.sh"
  exit 1
fi

CLEANING_TYPE=""
if [ $# -ge 1 ]; then CLEANING_TYPE=$1; fi

if [ "CLEANING_TYPE" = "" ]; then
  echo "ERROR: Invalid option, use bin/clean.bat <docker|files>"
  exit 1
fi

if [ "CLEANING_TYPE" = "docker" ]; then
  echo "== Cleaning unused docker resources"
  sudo docker image prune --force
  sudo docker volume prune --force
fi

if [ "CLEANING_TYPE" = "files" ]; then
  echo "== Cleaning unused files"
  sudo docker compose exec django /bin/sh -c "python ./bin/scripts/clean_files.py"
fi