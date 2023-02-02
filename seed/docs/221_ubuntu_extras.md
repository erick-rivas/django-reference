## Ubuntu Server - 20.04 (Extras)

This file contains guides to deploy project to a (Ubuntu Server)

### Enable remote access to database via SSL

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

#### Supervisor setup (Needed for celery)

-   Modify /etc/supervisor/conf.d/celery_worker.conf with the following structure
```
[program:celery]
directory=#API_DIR#
command=#API_DIR#/.venv/bin/celery -A seed.app worker -l INFO -B

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

-   Copy `seed/docs/assets/ubuntu/deploy.sh` in server root folder

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