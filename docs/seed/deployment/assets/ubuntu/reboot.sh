#!/bin/bash

# Restart server
sudo supervisorctl restart celery
sudo systemctl restart gunicorn
sudo systemctl restart nginx