#!/bin/bash

GIT_PATH="origin"
if [ $# -ge 1 ]; then GIT_PATH=$1; fi

API_DIR="###"
WEB_DIR="###"
# Update project
cd $API_DIR
sudo git pull $GIT_PATH dev
# shellcheck disable=SC1090
. "$(pwd)"/.venv/bin/activate
pip3 install -r requirements.txt
python3 manage.py migrate
python3 manage.py loaddata models/fixtures/*.yaml
python3 manage.py collectstatic --noinput

# Optional (Uncomment for reactJS integration)
# cd $WEB_DIR
# npm run-script build
# sudo rm -rf  $API_DIR/reactjs
# sudo mv $WEB_DIR/build $API_DIR/reactjs
# cd $API_DIR
# python3 manage.py collectstatic --noinput

# Restart server
sudo supervisorctl restart celery
sudo systemctl restart gunicorn
sudo systemctl restart nginx