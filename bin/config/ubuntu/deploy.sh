#!/bin/sh

# Update project
sudo git pull origin dev
PWD=`pwd`
. $PWD/.venv/bin/activate
pip3 install -r requirements.txt
python3 manage.py migrate
python3 manage.py loaddata models/fixtures/*.yaml
python3 manage.py collectstatic

# Restart server
sudo systemctl restart gunicorn
sudo systemctl restart nginx