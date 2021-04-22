#!/bin/bash
echo "== Analyzing code coverage"
RUNNING=$(docker-compose -f bin/docker/docker-compose.dev.yml ps --services --filter "status=running")
if [ $RUNNING -z ]; then
  echo "ERROR: Before executing bin/coverage.sh, start server with bin/start.sh"
  exit 1
fi
sudo docker-compose -f bin/docker/docker-compose.dev.yml exec django /bin/sh -c "coverage run --omit='.venv/*,bin/*,tests/*,*__init__*,seed/*, app/*' manage.py test"
sudo docker-compose -f bin/docker/docker-compose.dev.yml exec django /bin/sh -c "coverage report -m"