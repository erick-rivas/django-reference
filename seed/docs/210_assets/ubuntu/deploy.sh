#!/bin/sh

# Update project
cd <DJANGO_DIR>
sudo git pull origin dev
# shellcheck disable=SC1090
. "$(pwd)"/.venv/bin/activate
pip3 install -r requirements.txt
python3 manage.py migrate
python3 manage.py loaddata models/fixtures/*.yaml
python3 manage.py collectstatic

# Optional (Update app for single server)
# cd <REACT_DIR>
# sudo git pull origin dev
# npm run-script build
# rm -rf  /home/ubuntu/<DJANGO_DIR>/reactjs
# mv <REACT_DIR>/build <DJANGO_DIR>/reactjs
# cd <DJANGO_DIR>
# python3 manage.py collectstatic

# Restart server
sudo systemctl restart gunicorn
sudo systemctl restart nginx

# Optional (Restart celery)
# sudo supervisorctl restart celery