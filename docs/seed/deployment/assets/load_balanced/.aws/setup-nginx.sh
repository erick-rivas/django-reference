#!/bin/bash
# Setup Nginx for API

SERVER_NAME="<PROJECT_DOMAIN>"

NGINX_NORMAL="
server {
    listen 80;
    server_name $SERVER_NAME;
    client_max_body_size 75M;
    fastcgi_read_timeout 3000;
    proxy_read_timeout 3000;

    location ~ ^/(login|admin\/login\/) {
        include proxy_params;
        proxy_pass http://localhost:8008;
    }

    location /ws/ {
        proxy_http_version 1.1;
        proxy_set_header Upgrade \$http_upgrade;
        proxy_set_header Connection "upgrade";
        proxy_redirect off;
        proxy_pass http://localhost:8008;
    }

    location / {
        include proxy_params;
        proxy_pass http://localhost:8008;
    }
}
"
echo "$NGINX_NORMAL" | sudo tee "/etc/nginx/sites-available/app"

sudo sed -i 's/#\s*server_names_hash_bucket_size 64;/server_names_hash_bucket_size 256;/' /etc/nginx/nginx.conf
sudo ln -s /etc/nginx/sites-available/app /etc/nginx/sites-enabled
sudo systemctl restart nginx

sleep 4
sudo nginx -t