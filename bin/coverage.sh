#!/bin/bash
# Seed builder
# AUTO_GENERATED (Read only)

RUNNING=$(sudo docker compose ps --services --filter "status=running")
if [ $RUNNING -z ]; then
  echo "ERROR: Before executing bin/coverage.sh, start server with bin/start.sh"
  exit 1
fi

SUB_PATH="None"
if [ $# -ge 1 ]; then SUB_PATH=$1; fi

if [ $SUB_PATH = "None" ]; then
  echo "== Executing full coverage"
  sudo docker compose exec django /bin/sh -c "coverage run --omit='.venv/*,bin/*,tests/*,*__init__*,seed/*, app/*' manage.py test"
else
  echo "== Executing /$SUB_PATH coverage"
  sudo docker compose exec django /bin/sh -c "coverage run --omit='.venv/*,bin/*,tests/*,*__init__*,seed/*, app/*' manage.py test $SUB_PATH/ "
fi

sudo docker compose exec django /bin/sh -c "coverage report -m"
sudo docker compose exec django /bin/sh -c "coverage xml"