#!/bin/sh

# Update project
cd <SERVER_DIR>
sudo git pull origin dev
# shellcheck disable=SC1090
. "$(pwd)"/.venv/bin/activate
pip3 install -r requirements.txt
python3 manage.py migrate
python3 manage.py loaddata models/fixtures/*.yaml
python3 manage.py collectstatic

# Optional (Update app for single server)
# cd <APP_DIR>
# npm run_script build
# mv <APP_DIR>/build <SERVER_DIR>/reactjs

# Restart server
sudo systemctl restart gunicorn
sudo systemctl restart nginx