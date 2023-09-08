#!/bin/bash
# Seed builder
# AUTO_GENERATED (Read only)

RUNNING=$(sudo docker compose ps --services --filter "status=running")
if [ $RUNNING -z ]; then
  echo "ERROR: Before executing bin/psql.sh, start server with bin/start.sh"
  exit 1
fi

echo "== Opening db console"
sudo docker compose exec django /bin/sh -c "python manage.py dbshell"