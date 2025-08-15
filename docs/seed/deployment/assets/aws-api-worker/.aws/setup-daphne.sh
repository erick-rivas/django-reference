#!/bin/bash
# Setup Daphne service (websockets) for API

DAPHNE_SERVICE="
[Unit]
Description=daphne daemon
After=network.target

[Service]
User=ubuntu
Group=ubuntu
WorkingDirectory=/home/ubuntu/<PROJECT>
ExecStart=/home/ubuntu/<PROJECT>/.venv/bin/daphne \
          --bind 0.0.0.0 \
          --port 8008 \
          seed.app.asgi:application

Restart=on-failure

StandardOutput=append:/var/log/daphne.access.log
StandardError=append:/var/log/daphne.error.log

[Install]
WantedBy=multi-user.target
"
echo "$DAPHNE_SERVICE" | sudo tee "/etc/systemd/system/daphne.service"

sudo touch /var/log/daphne.error.log /var/log/daphne.access.log
sudo chmod 666 /var/log/daphne.error.log /var/log/daphne.access.log
sudo systemctl daemon-reload
sudo systemctl restart daphne.service
sudo systemctl status daphne --no-pager

echo "Wait 10 seconds and check that daphne service works..."
sleep 10