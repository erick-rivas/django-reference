#!/bin/sh
echo "== Making & executing migrations"
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py loaddata models/fixtures/*.yaml

echo "== Filling database"
python3 manage.py loaddata models/fixtures/*.yaml