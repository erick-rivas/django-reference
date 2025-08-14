#!/bin/bash
# Setup Celery workers for background tasks

sudo apt-get install supervisor

CELERY_WORKER="
[program:celery]
directory=/home/ubuntu/<PROJECT>
command=/home/ubuntu/<PROJECT>/.venv/bin/celery -A seed.app worker -l INFO -B

user=ubuntu
numprocs=1
stdout_logfile=/var/log/celery.access.log
stderr_logfile=/var/log/celery.error.log
stdout_logfile_maxbytes=50
stderr_logfile_maxbytes=50
stdout_logfile_backups=10
stderr_logfile_backups=10
autostart=true
autorestart=true
startsecs=10

stopwaitsecs = 7200
stopasgroup=true
priority=1000
"
echo "$CELERY_WORKER" | sudo tee "/etc/supervisor/conf.d/celery_worker.conf"

sudo touch /var/log/celery.error.log /var/log/celery.access.log
sudo chmod 666 /var/log/celery.error.log /var/log/celery.access.log

sudo supervisorctl reread
sudo supervisorctl update
sudo supervisorctl start all
sudo supervisorctl restart celery

sleep 4
sudo supervisorctl status all

sudo chmod -R 777 /home/ubuntu/<PROJECT>