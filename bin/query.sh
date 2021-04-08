#!/bin/bash
echo "== Opening psql console"
docker-compose -f bin/docker/docker-compose.dev.yml run django /bin/sh -c "python manage.py dbshell"