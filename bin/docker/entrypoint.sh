#!/bin/sh
# Seed builder
# AUTO_GENERATED (Read only)

echo "== Making & executing migrations"
python3 manage.py makemigrations
python3 manage.py migrate

echo "== Filling database"
python3 manage.py loaddata models/fixtures/*.yaml