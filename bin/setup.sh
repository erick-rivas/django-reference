#!/bin/bash

echo "== Configure docker .env"
DJANGO_PORT=8008
POSTGRES_PORT=5435
REDIS_PORT=6377
if [ $# -ge 1 ]; then
  DJANGO_PORT=$1
fi
if [ $# -ge 2 ]; then
  DB_PORT=$2
fi
if [ $# -ge 3 ]; then
  REDIS_PORT=$3
fi
sudo rm bin/docker/.env
sudo rm bin/docker/.env-info
echo "# DOCKER PORTS" > "bin/docker/.env"
echo "### MODIFY WITH WITH $ bin/setup <DJANGO_PORT> <POSTGRES_PORT> <REDIS_PORT> ###" >> "bin/docker/.env"
echo "" >> "bin/docker/.env"
echo "DJANGO_PORT=$DJANGO_PORT" >> "bin/docker/.env"
echo "POSTGRES_PORT=$POSTGRES_PORT" >> "bin/docker/.env"
echo "REDIS_PORT=$REDIS_PORT" >> "bin/docker/.env"

echo "$DJANGO_PORT" > "bin/docker/.env-port"

echo "== Deleting previous containers"
docker-compose -f bin/docker/docker-compose.dev.yml down

echo "== Building project"
docker-compose -f bin/docker/docker-compose.dev.yml build

echo "== Setting execute permissions to bin"
docker-compose -f bin/docker/docker-compose.dev.yml run django /bin/sh -c "chmod +x bin/*.sh;chmod +x bin/docker/*.sh"

echo "== Creating .env.devs"
docker-compose -f bin/docker/docker-compose.dev.yml run django /bin/sh -c  "bin/docker/env-dev.sh $DJANGO_PORT $POSTGRES_PORT $REDIS_PORT"

echo "== Starting services"
docker-compose -f bin/docker/docker-compose.dev.yml up -d

echo "== Executing entrypoint.sh (make & run migrations)"
docker-compose -f bin/docker/docker-compose.dev.yml exec django /bin/sh -c "bin/docker/entrypoint.sh"

echo "== Loading dev fixtures (admin)"
docker-compose -f bin/docker/docker-compose.dev.yml exec django /bin/sh -c "python manage.py loaddata bin/docker/fixtures-dev.yaml"

echo "== Generating docs"
docker-compose -f bin/docker/docker-compose.dev.yml exec django /bin/sh -c "sphinx-build -E -b html ./docs ./.data/docs"

echo "== Stopping services"
docker-compose -f bin/docker/docker-compose.dev.yml stop

echo ""
echo "== Setup completed (Start server with bin/start.sh)"
echo ""