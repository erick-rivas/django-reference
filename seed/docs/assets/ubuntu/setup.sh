#!/bin/bash
if [ $# -lt 3 ]; then
  echo "Missing params"
  echo "Call $ ./bin/setup.sh <db_name> <db_user> <db_password>"
  exit 1
fi

DB_NAME=$1
DB_USER=$2
DB_PASSWORD=$3

echo "== Creating postgres database"
echo "Enter postgres password ($DB_PASSWORD)"
createdb -h localhost -p 5432 -U "$DB_USER" "$DB_NAME"

echo "== Creating virtual environment"
python3 -m venv .venv
# shellcheck disable=SC1090
. "$(pwd)"/.venv/bin/activate

echo "== Installing dependencies"
python3 -m pip install --upgrade pip
pip3 install -r requirements.txt

echo "== Creating & configuring env.dev file"
cp .env.example .env.dev
sed -i "s/DB_NAME=/DB_NAME=$DB_NAME/" ".env.dev"
sed -i "s/DB_USER=/DB_USER=$DB_USER/" ".env.dev"
sed -i "s/DB_PASSWORD=/DB_PASSWORD=$DB_PASSWORD/" ".env.dev"
sed -i "s/DB_HOST=/DB_HOST=localhost/" ".env.dev"
sed -i "s/SECRET_KEY=/SECRET_KEY=fupswltefA9efredrufihUSTOwamc/" ".env.dev"

echo "== Making & executing migrations"
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py loaddata models/fixtures/*.yaml

echo "== Filling database"
python3 manage.py loaddata models/fixtures/*.yaml