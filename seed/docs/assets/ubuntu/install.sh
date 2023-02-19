#!/bin/bash
if [ $# -lt 5 ]; then
  echo "Missing params"
  echo "Call $ ./bin/install.sh <server_name> <db_name> <db_user> <db_password>"
  exit 1
fi

SERVER_NAME=$1
DB_NAME=$2
DB_USER=$3
DB_PASSWORD=$4
API_DIR=$(pwd)

#####
echo "== Installing dependencies"
####

# General dependencies
sudo apt update
sudo apt install curl git-core zlib1g-dev build-essential libssl-dev libreadline-dev libyaml-dev libsqlite3-dev sqlite3 libxml2-dev libxslt1-dev libcurl4-openssl-dev software-properties-common libffi-dev yarn

# Install python tools
sudo apt update
sudo apt install python3-pip python3-dev python3-venv libpq-dev nginx nginx-extras

# Install postgreSQL
sudo apt install wget ca-certificates
wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -
sudo sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt/ `lsb_release -cs`-pgdg main" >> /etc/apt/sources.list.d/pgdg.list'
sudo apt update
sudo apt install postgresql postgresql-contrib libpq-dev

# Install redis & supervisor
sudo apt-get install redis-server supervisor
redis-cli ping
sudo systemctl enable redis-server.service

#####
echo "== Database setup"
#####

# Create user
sudo -u postgres psql -c "create user $DB_USER with encrypted password '$DB_PASSWORD'"
sudo -u postgres psql -c "alter role $DB_USER with superuser"

# Open 5432 port
sudo sed -i "s/#listen_addresses = 'localhost'/listen_addresses = '*'/" "/etc/postgresql/15/main/postgresql.conf"
sudo sh -c 'echo "host    all             all             0.0.0.0/0          md5" >> "/etc/postgresql/15/main/pg_hba.conf"'
sudo service postgresql restart

#####
echo "== Project setup"
#####

chmod 777 $API_DIR/seed/docs/assets/ubuntu/setup.sh
$API_DIR/seed/docs/assets/ubuntu/setup.sh $DB_NAME $DB_USER $DB_PASSWORD

#####
echo "== Gunicorn setup"
#####

GUNICORN_SOCKET="
[Unit]
Description=gunicorn socket

[Socket]
ListenStream=/run/gunicorn.sock

[Install]
WantedBy=sockets.target
"
echo "$GUNICORN_SOCKET" | sudo tee "/etc/systemd/system/gunicorn.socket"

GUNICORN_SERVICE="
[Unit]
Description=gunicorn daemon
Requires=gunicorn.socket
After=network.target

[Service]
User=ubuntu
Group=ubuntu
WorkingDirectory=$API_DIR
ExecStart=$API_DIR/.venv/bin/gunicorn \
          --log-level debug \
          --access-logfile /var/log/gunicorn.access.log \
          --workers 3 \
          --error-logfile /var/log/gunicorn.error.log \
          --capture-output \
          --bind unix:/run/gunicorn.sock \
          seed.app.wsgi:application

[Install]
WantedBy=multi-user.target
"
echo "$GUNICORN_SERVICE" | sudo tee "/etc/systemd/system/gunicorn.service"

sudo touch /var/log/gunicorn.error.log /var/log/gunicorn.access.log
sudo chmod 666 /var/log/gunicorn.error.log /var/log/gunicorn.access.log
sudo systemctl start gunicorn.socket
sudo systemctl enable gunicorn.socket
sudo systemctl restart gunicorn
sudo systemctl status gunicorn --no-pager

echo "Wait 10 seconds and check that gunicorn service works..."
sleep 10

#####
echo "== Nginx setup"
#####

NGINX_NORMAL="
server {
    listen 80;
    server_name $SERVER_NAME;
    client_max_body_size 75M;
    fastcgi_read_timeout 5000;
    proxy_read_timeout 5000;

    location / {
        include proxy_params;
        proxy_pass http://unix:/run/gunicorn.sock;
    }
}
"
echo "$NGINX_NORMAL" | sudo tee "/etc/nginx/sites-available/app"

sudo ln -s /etc/nginx/sites-available/app /etc/nginx/sites-enabled
sudo systemctl restart nginx

sleep 4
sudo nginx -t

#####
echo "== Supervisor setup"
#####

CELERY_WORKER="
[program:celery]
directory=$API_DIR
command=$API_DIR/.venv/bin/celery -A seed.app worker -l INFO -B

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

echo ""
echo "== Installation completed (Continue with .envs adjustments)"
echo ""