## Ubuntu Server - 20.04

This file contains guides to deploy project to a (Ubuntu Server)

### Server installation

#### Dependencies

-   Install general dependencies
```bash
sudo apt update
sudo apt install curl git-core zlib1g-dev build-essential libssl-dev libreadline-dev libyaml-dev libsqlite3-dev sqlite3 libxml2-dev libxslt1-dev libcurl4-openssl-dev software-properties-common libffi-dev yarn
```

-   Install python and server tools
>   Recommended version python 3.8.x

```bash
sudo apt update
sudo apt install python3-pip python3-dev python3-venv libpq-dev nginx nginx-extras
```

##### Postgresql

-   Install dependencies
>   Recommended version PostgreSQL 14
```bash
sudo apt install wget ca-certificates
wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -
sudo sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt/ `lsb_release -cs`-pgdg main" >> /etc/apt/sources.list.d/pgdg.list'

sudo apt update
sudo apt install postgresql postgresql-contrib libpq-dev
```

-   Create user
```bash
sudo -u postgres psql
postgres=# create user #DB_USER# with encrypted password '#DB_PASSWORD#';
postgres=# ALTER ROLE #DB_USER# WITH SUPERUSER;
postgres=# exit;
```

-   To enable remote access, open 5432 port and configure postgres files
```bash
sudo vim /etc/postgresql/<PG_VERSION>/main/postgresql.conf
-- listen_addresses = '*'
```

```bash
sudo vim /etc/postgresql/<PG_VERSION>/main/pg_hba.conf
-- host    all             all             0.0.0.0/0          md5
```

```bash
sudo service postgresql restart
```

-   To enable ssl
>   It needs certbot implementation
```bash
sudo cp /etc/letsencrypt/live/#SERVER_NAME#/cert.pem /etc/postgresql/<PG_VERSION>/main/server.crt
sudo cp /etc/letsencrypt/live/#SERVER_NAME#/privkey.pem /etc/postgresql/<PG_VERSION>/main/server.key
sudo chown postgres:postgres /etc/postgresql/<PG_VERSION>/main/server.crt /etc/postgresql/<PG_VERSION>/main/server.key
sudo chmod 400 /etc/postgresql/<PG_VERSION>/main/server.crt /etc/postgresql/<PG_VERSION>/main/server.key
```

```bash
sudo vim /etc/postgresql/<PG_VERSION>/main/postgresql.conf
-- ssl = on
-- ssl_cert_file = '/etc/postgresql/<PG_VERSION>/main/server.crt'
-- ssl_key_file = '/etc/postgresql/<PG_VERSION>/main/server.key'
```

```bash
sudo vim /etc/postgresql/<PG_VERSION>/main/pg_hba.conf
-- hostssl    all             all             0.0.0.0/0          md5
```

##### Redis (celery-optional)

-   Install dependencies
```bash
sudo apt-get install redis-server supervisor
redis-cli ping
sudo systemctl enable redis-server.service
```

### Production environment

-  For  production set the environment variable IS_PROD=true
```bash
vim ~/.bash_profile
export IS_PROD=true
```

#### Project installation

-   Clone repository
-   Execute setup script ```./seed/docs/210_assets/ubuntu/setup.sh #DB_NAME# #DB_USER# #DB_PASSWORD#```
-   Adjust .env.dev or .env.prod for production environment and setup the project variables
```
# Important settings
SERVER_URL=#SERVER_URL#
CLIENT_URL=#CLIENT_URL#
SECRET_KEY=#ANY_SECRET_KEY#
ENABLE_AUTH=true/false
```
		

#### Gunicorn configuration

-   Modify /etc/systemd/system/gunicorn.socket with the following structure

```
[Unit]
Description=gunicorn socket

[Socket]
ListenStream=/run/gunicorn.sock

[Install]
WantedBy=sockets.target
```

-   Modify /etc/systemd/system/gunicorn.service with the following structure
```
[Unit]
Description=gunicorn daemon
Requires=gunicorn.socket
After=network.target

[Service]
User=#SO_USER#
Group=#SO_USER#
WorkingDirectory=#PROJECT_DIR#
ExecStart=#PROJECT_DIR#/.venv/bin/gunicorn \
          --log-level debug \
          --access-logfile /var/log/gunicorn.access.log \
          --workers 3 \
          --error-logfile /var/log/gunicorn.error.log \
          --capture-output \
          --bind unix:/run/gunicorn.sock \
          seed.app.wsgi:application

[Install]
WantedBy=multi-user.target
```
>   *To obtain the user and group of OS, use ```id``` command (For aws-ec2=ubuntu,ubuntu)*

-   Create gunicorn log files ```sudo touch /var/log/gunicorn.error.log /var/log/gunicorn.access.log```

-   Set read/write permissions to log files ```sudo chmod 666 /var/log/gunicorn.error.log /var/log/gunicorn.access.log```

-   Init gunicorn socket
``` bash
sudo systemctl start gunicorn.socket
sudo systemctl enable gunicorn.socket
```

-   Check gunicorn status `sudo systemctl status gunicorn`

-   Restart gunicorn `sudo systemctl restart gunicorn`

#### Nginx configuration

-  Modify /etc/nginx/sites-available/app with the following structure
```
server {
    listen 80;
    server_name #SERVER_NAME#;
    client_max_body_size 75M;
    fastcgi_read_timeout 5000;
    proxy_read_timeout 5000;

    location / {
        include proxy_params;
        proxy_pass http://unix:/run/gunicorn.sock;
    }
}
```

-   Create a link to sites-enabled
``` bash
sudo ln -s /etc/nginx/sites-available/app /etc/nginx/sites-enabled
```

-   Check nginx status `sudo nginx -t`

-   Restart nginx `sudo systemctl restart nginx`

#### Supervisor configuration (celery-optional)

-   Modify /etc/supervisor/conf.d/celery_worker.conf with the following structure
```
[program:celery]
directory=#PROJECT_DIR#
command=#PROJECT_DIR#/.venv/bin/celery -A seed.app worker -l INFO -B

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
```

-   Create celery log files ```sudo touch /var/log/celery.error.log /var/log/celery.access.log```

-   Set read/write permissions to log files ```sudo chmod 666 /var/log/celery.error.log /var/log/celery.access.log```

-   Restart supervisor
``` bash
sudo supervisorctl reread
sudo supervisorctl update
sudo supervisorctl start all
```

-   Check supervisor status `sudo supervisorctl status all`

-   Restart supervisor celery `sudo supervisorctl restart celery`

#### ReactJS configuration (optional)

-   Check reference [documentation](https://github.com/erick-rivas/reactjs-reference/blob/master/src/seed/docs/220_ubuntu.md)

### SSL

To enable a https connection

#### Configure certbot

-   Install certbot
```bash
sudo apt update
sudo snap install core; sudo snap refresh core
sudo snap install --classic certbot
sudo ln -s /snap/bin/certbot /usr/bin/certbot
```

-   Request a certificate `sudo certbot certonly --nginx`

#### Configure nginx

-   Modify /etc/nginx/sites-available/app with the following structure
```
server {
    listen 443 ssl default_server;
    server_name #SERVER_NAME#;
    client_max_body_size 75M;
    fastcgi_read_timeout 3000;
    proxy_read_timeout 3000;
    more_clear_headers Server;
    server_tokens off;

    ssl_protocols TLSv1.2 TLSv1.3;
    ssl_certificate /etc/letsencrypt/live/#SERVER_NAME#/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/#SERVER_NAME#/privkey.pem;
    include /etc/letsencrypt/options-ssl-nginx.conf;
    ssl_dhparam /etc/letsencrypt/ssl-dhparams.pem;

    location / {
        include proxy_params;
        proxy_pass http://unix:/run/gunicorn.sock;
    }
}
server {
    listen 80;
    server_name #SERVER_NAME#;
    return 301 https://#SERVER_NAME#$request_uri;
}
```

-   Restart nginx `sudo systemctl restart nginx`

### Deployment

-   Copy `seed/docs/210_assets/ubuntu/deploy.sh` in server root folder

-   Run deployment script `./deploy.sh`

#### Server logs

-   To watch gunicorn logs (main) `tail -f /var/log/gunicorn.access.log`
-   To watch nginx logs `tail -f /var/log/nginx/access.log`

### References

-   Gunicorn-nginx tutorial [https://www.digitalocean.com/community/tutorials/how-to-set-up-django-with-postgres-nginx-and-gunicorn-on-ubuntu-18-04#creating-systemd-socket-and-service-files-for-gunicorn](https://www.digitalocean.com/community/tutorials/how-to-set-up-django-with-postgres-nginx-and-gunicorn-on-ubuntu-18-04#creating-systemd-socket-and-service-files-for-gunicorn)
-   PostgreSQL SSL [https://www.vultr.com/docs/use-ssl-encryption-with-postgresql-on-ubuntu-20-04/](https://www.vultr.com/docs/use-ssl-encryption-with-postgresql-on-ubuntu-20-04/)
-   Increase storage EC2 [https://medium.com/@m.yunan.helmy/increase-the-size-of-ebs-volume-in-your-ec2-instance-3859e4be6cb7] (https://medium.com/@m.yunan.helmy/increase-the-size-of-ebs-volume-in-your-ec2-instance-3859e4be6cb7)

### See also

-   [Deployment - AWS ElasticBeanstalk single instance](./230_eb_single_instance.md)
-   [Deployment - AWS ElasticBeanstalk load balanced](./240_eb_load_balanced.md)