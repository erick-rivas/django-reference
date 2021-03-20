#!/bin/bash
if [ $# -lt 3 ]; then
  echo "Missing params"
  echo "Call $ ./bin/setup.sh <db_name> <db_username> <db_password>"
  exit 1
fi
echo "== Creating postgres database"
echo "Enter postgres password"
createdb -h localhost -p 5432 -U $2 $1

echo "== Creating virtual environment"
python3 -m venv .venv
PWD=`pwd`
activate () {
    . $PWD/.venv/bin/activate
}
activate

echo "== Installing dependencies"
python3 -m pip install --upgrade pip
pip3 install -r requirements.txt

echo "== Creating & configuring env.dev file"
cp .env.example .env.dev
sed -i "s/DB_NAME=/DB_NAME=$1/" ".env.dev"
sed -i "s/DB_USER=/DB_USER=$2/" ".env.dev"
sed -i "s/DB_PASSWORD=/DB_PASSWORD=$3/" ".env.dev"

echo "== Making & executing migrations"
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py loaddata models/fixtures/*.yaml