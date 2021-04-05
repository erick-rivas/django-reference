## Ubuntu Server - 18.04

This file contains guides to deploy project to a (Ubuntu Server)

### Server installation

#### Dependencies

- Connect to server

```bash
ssh <USER@SERVER_URL>
```

- Install general dependencies
```bash
sudo apt update
sudo apt install curl git-core zlib1g-dev build-essential libssl-dev libreadline-dev libyaml-dev libsqlite3-dev sqlite3 libxml2-dev libxslt1-dev libcurl4-openssl-dev software-properties-common libffi-dev nodejs yarn
```

-   Install python and django
```bash
sudo apt update
sudo apt install python3-pip python3-dev python3-venv libpq-dev postgresql postgresql-contrib nginx curl
```

##### Postgresql

- Install dependencies
```bash
sudo apt install wget ca-certificates
wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -
sudo sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt/ `lsb_release -cs`-pgdg main" >> /etc/apt/sources.list.d/pgdg.list'

sudo apt update
sudo apt install postgresql postgresql-contrib libpq-dev
```

-  Create user and database
```bash
sudo -u postgres psql
postgres=# create user admin with encrypted password 'password';
postgres=# ALTER ROLE admin WITH SUPERUSER;
```

#### Project installation

-   Clone repository and follow installation steps in [general docs](./010_general.md)


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
          --access-logfile - \
          --workers 3 \
          --bind unix:/run/gunicorn.sock \
          app.wsgi:application

[Install]
WantedBy=multi-user.target
```
>  *To check os user and group user id command (For aws-ec2=ubuntu,ubuntu)*
> 
-  Init gunicorn socket
``` bash
sudo systemctl start gunicorn.socket
sudo systemctl enable gunicorn.socket
```

-  Check gunicorn status
``` bash
sudo systemctl status gunicorn
```

-  Restart gunicorn
``` bash
sudo systemctl restart gunicorn
```


#### Nginx configuration

-  Modify /etc/nginx/sites-available/app with the following structure
```
server {
    listen 80;
    server_name #SERVER_NAME#;
    client_max_body_size 75M;
    fastcgi_read_timeout 3000;
    proxy_read_timeout 3000;

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

-  Check nginx status
``` bash
sudo nginx -t
```

-  Restart nginx
``` bash
sudo systemctl restart nginx
```

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

-   Request a certificate
```bash
sudo certbot --nginx
```

#### Configure nginx

-  Modify /etc/nginx/sites-available/app with the following structure
```
server {
    listen 443 ssl default_server;
    ssl_protocols TLSv1.2 TLSv1.3;
    server_name #SERVER_NAME#;
    client_max_body_size 75M;
    fastcgi_read_timeout 3000;
    proxy_read_timeout 3000;   

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

-  Restart nginx
``` bash
sudo systemctl restart nginx
```

### Deployment

- Connect to server
```bash
ssh #USER@SERVER_URL#
```

-   Paste `bin/config/ubuntu/deploy.sh` in `bin` folder

-   Run deployment script
```bash
./bin/deploy.sh
```

### References

-   Gunicorn-nginx tutorial [https://www.digitalocean.com/community/tutorials/how-to-set-up-django-with-postgres-nginx-and-gunicorn-on-ubuntu-18-04#creating-systemd-socket-and-service-files-for-gunicorn](https://www.digitalocean.com/community/tutorials/how-to-set-up-django-with-postgres-nginx-and-gunicorn-on-ubuntu-18-04#creating-systemd-socket-and-service-files-for-gunicorn)