#!/bin/bash

sudo chmod -R 777 /home/ubuntu/<PROJECT>/
cd /home/ubuntu/<PROJECT>/
. /home/ubuntu/<PROJECT>/.venv/bin/activate

python3 manage.py migrate
python3 manage.py loaddata models/fixtures/*.yaml
python3 manage.py collectstatic --noinput

sudo systemctl restart daphne
sudo systemctl restart nginx