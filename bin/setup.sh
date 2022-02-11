#!/bin/bash
# Seed builder
# AUTO_GENERATED (Read only)

echo "== Configuring docker .env"
DJANGO_PORT=8008
POSTGRES_PORT=5435
REDIS_PORT=6377
SERVER_URL="http://localhost:8008"
CLIENT_URL="http://localhost:3003"
IS_PROD=false

if [ $# -ge 1 ]; then DJANGO_PORT=$1; fi
if [ $# -ge 2 ]; then POSTGRES_PORT=$2; fi
if [ $# -ge 3 ]; then REDIS_PORT=$3; fi
if [ $# -ge 4 ]; then SERVER_URL=$4; fi
if [ $# -ge 5 ]; then CLIENT_URL=$5; fi
if [ $# -ge 6 ]; then IS_PROD=$6; fi

echo "== Creating docker .envs"
sudo rm bin/docker/.env
sudo rm bin/docker/.port
echo "# DOCKER PORTS" > "bin/docker/.env"
echo "### MODIFY WITH WITH $ bin/setup DJANGO_PORT POSTGRES_PORT REDIS_PORT IS_PROD ###" >> "bin/docker/.env"
echo "" >> "bin/docker/.env"
echo "DJANGO_PORT=$DJANGO_PORT" >> "bin/docker/.env"
echo "POSTGRES_PORT=$POSTGRES_PORT" >> "bin/docker/.env"
echo "REDIS_PORT=$REDIS_PORT" >> "bin/docker/.env"
echo "IS_PROD=$IS_PROD" >> "bin/docker/.env"

echo "### MODIFY WITH WITH $ bin/setup DJANGO_PORT ###" >> "bin/docker/.port"
echo "$DJANGO_PORT" > "bin/docker/.port"

echo "== Deleting previous containers"
sudo docker-compose -f bin/docker/docker-compose-dev.yml down

echo "== Building project"
sudo docker-compose -f bin/docker/docker-compose-dev.yml build

echo "== Setting execute permissions to bin"
sudo docker-compose -f bin/docker/docker-compose-dev.yml run django_reference_django /bin/sh -c "chmod +x bin/*.sh;chmod +x bin/docker/*.sh"

echo "== Creating .env.devs"
sudo docker-compose -f bin/docker/docker-compose-dev.yml run django_reference_django /bin/sh -c  "bin/docker/env-dev.sh $DJANGO_PORT $POSTGRES_PORT $REDIS_PORT $SERVER_URL $CLIENT_URL"

echo "== Starting services"
sudo docker-compose -f bin/docker/docker-compose-dev.yml up -d

echo "== Executing db update (make & run migrations)"
sudo docker-compose -f bin/docker/docker-compose-dev.yml exec django_reference_django /bin/sh -c "bin/docker/db-update.sh"

echo "== Loading dev fixtures (admin)"
sudo docker-compose -f bin/docker/docker-compose-dev.yml exec django_reference_django /bin/sh -c "python manage.py loaddata bin/docker/fixtures-dev.yaml"

echo "== Generating docs"
sudo docker-compose -f bin/docker/docker-compose-dev.yml exec django_reference_django /bin/sh -c "sphinx-build -E -b html ./docs ./.data/docs"

echo "== Removing root permissions"
sudo chown -R $(whoami) .

echo "== Installing local dependencies"
python3 -m venv .venv
. "$(pwd)"/.venv/bin/activate
python3 -m pip install --upgrade pip
pip3 install -r requirements.txt

echo "== Cleaning services"
sudo docker-compose -f bin/docker/docker-compose-dev.yml stop

echo ""
echo "== Setup completed (Start server with bin/start.sh)"
echo ""