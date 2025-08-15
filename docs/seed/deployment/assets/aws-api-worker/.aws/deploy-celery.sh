#!/bin/bash

sudo chmod -R 777 /home/ubuntu/<PROJECT>/
cd /home/ubuntu/<PROJECT>
. /home/ubuntu/<PROJECT>/.venv/bin/activate
sudo supervisorctl restart celery