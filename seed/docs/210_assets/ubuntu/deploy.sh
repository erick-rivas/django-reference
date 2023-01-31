#!/bin/sh

# Update project
cd <API_DIR>
# shellcheck disable=SC1090
. "$(pwd)"/.venv/bin/activate
pip3 install -r requirements.txt
python3 manage.py migrate
python3 manage.py loaddata models/fixtures/*.yaml
python3 manage.py collectstatic

# Optional (Uncomment for reactJS integration)
# cd <WEB_DIR>
# sudo git pull origin dev
# npm run-script build
# sudo rm -rf  /home/ubuntu/<API_DIR>/reactjs
# sudo mv <WEB_DIR>/build <API_DIR>/reactjs
# cd <API_DIR>
# python3 manage.py collectstatic

# Restart server
sudo systemctl restart gunicorn
sudo systemctl restart nginx

# Optional (Uncomment for celery integration)
# sudo supervisorctl restart celery