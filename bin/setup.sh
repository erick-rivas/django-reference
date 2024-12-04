#!/bin/bash
### __Seed builder__
# AUTO_GENERATED
# Add custom commands at the end

echo "== Configuring docker .env"
DJANGO_PORT=8008
POSTGRES_PORT=5435
REDIS_PORT=6377
SERVER_URL="http://localhost:$DJANGO_PORT"
CLIENT_URL="http://localhost:3003"
IS_PROD=false

if [ $# -ge 1 ]; then DJANGO_PORT=$1; fi
if [ $# -ge 2 ]; then POSTGRES_PORT=$2; fi
if [ $# -ge 3 ]; then REDIS_PORT=$3; fi
if [ $# -ge 4 ]; then SERVER_URL=$4; fi
if [ $# -ge 5 ]; then CLIENT_URL=$5; fi
if [ $# -ge 6 ]; then IS_PROD=$6; fi

RUNNING=$(sudo docker ps)
if [ $RUNNING -z ]; then
  echo "ERROR: Before executing bin/setup.sh, start docker service"
  exit 1
fi

echo "== Creating docker .envs"
sudo rm .env
echo "# DOCKER SETTINGS" > ".env"
echo "### MODIFY WITH WITH $ bin/setup DJANGO_PORT POSTGRES_PORT REDIS_PORT IS_PROD ###" >> ".env"
echo "" >> ".env"
echo "COMPOSE_PROJECT_NAME=django_reference_backend" >> ".env"
echo "COMPOSE_DJANGO_PORT=$DJANGO_PORT" >> ".env"
echo "COMPOSE_POSTGRES_PORT=$POSTGRES_PORT" >> ".env"
echo "COMPOSE_REDIS_PORT=$REDIS_PORT" >> ".env"
echo "IS_PROD=$IS_PROD" >> ".env"

if [ ! -f debug_.py ]; then
  echo "# Temporary file for debugging, run with bin/debug.sh" -> "debug_.py"
fi

echo "== Deleting previous containers"
sudo docker compose down

echo "== Building project"
sudo docker compose build

echo "== Setting execute permissions to bin"
sudo docker compose run --rm django /bin/sh -c "chmod +x bin/*.sh;chmod +x bin/scripts/*.sh"

echo "== Initializing .envs"
sudo docker compose run --rm django /bin/sh -c  "bin/scripts/init_envs.sh $POSTGRES_PORT $REDIS_PORT $SERVER_URL $CLIENT_URL $IS_PROD"

echo "== Starting services"
sudo docker compose up -d

echo "== Executing db update (make & run migrations)"
sudo docker compose exec django /bin/sh -c "python manage.py makemigrations"
sudo docker compose exec django /bin/sh -c "python manage.py migrate"

echo "== Loading fixtures"
sudo docker compose exec django /bin/sh -c "python manage.py loaddata models/fixtures/.base.yaml"
sudo docker compose exec django /bin/sh -c "python manage.py loaddata models/fixtures/*.yaml"

echo "== Removing root permissions"
sudo chown -R $(whoami) .

echo "== Installing local dependencies"
if [ ! -d .venv ]; then
  python3 -m venv .venv
fi
. "$(pwd)"/.venv/bin/activate
python3 -m pip install --upgrade pip
pip3 install -r requirements.txt

if [ "$IS_PROD" = true ]; then
  echo "== Exporting prod statics"
  sudo docker compose exec django /bin/sh -c "python manage.py collectstatic"
fi

echo "== Cleaning setup"
sudo docker compose stop
sudo docker image prune --force
sudo docker volume prune --force

echo ""
echo "== Setup completed (Start server with bin/start.sh)"
echo ""

if [ "$IS_PROD" = true ]; then
  echo "***"
  echo "*** IMPORTANT: FOR SECURITY, CHANGE THE ADMIN PASSWORD IMMEDIATELY"
  echo "***"
  echo ""
fi

#  __End autogenerated__
#  Include commands after this block
###