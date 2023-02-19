#!/bin/bash
if [ $# -lt 1 ]; then
  echo "Missing params"
  echo "Call $ ./bin/install-ssl.sh <server_name>"
  exit 1
fi

SERVER_NAME=$1

echo "== Installing dependencies setup"
sudo apt update
sudo snap install core; sudo snap refresh core
sudo snap install --classic certbot
sudo ln -s /snap/bin/certbot /usr/bin/certbot

echo "== Certbot setup"
sudo certbot certonly --nginx

echo "== Nginx setup"

NGINX_SSL="
server {
    listen 443 ssl default_server;
    server_name $SERVER_NAME
    ;
    client_max_body_size 75M;
    fastcgi_read_timeout 3000;
    proxy_read_timeout 3000;
    more_clear_headers Server;
    server_tokens off;

    ssl_protocols TLSv1.2 TLSv1.3;
    ssl_certificate /etc/letsencrypt/live/$SERVER_NAME/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/$SERVER_NAME/privkey.pem;
    include /etc/letsencrypt/options-ssl-nginx.conf;
    ssl_dhparam /etc/letsencrypt/ssl-dhparams.pem;

    location / {
        include proxy_params;
        proxy_pass http://unix:/run/gunicorn.sock;
    }
}
server {
    listen 80;
    server_name $SERVER_NAME;
    return 301 https://$SERVER_NAME$request_uri;
}
"
echo "$NGINX_SSL" | sudo tee "/etc/nginx/sites-available/app"

sudo systemctl restart nginx