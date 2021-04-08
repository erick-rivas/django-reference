#!/bin/bash
echo "== Executing test cases"
docker-compose -f bin/docker/docker-compose.dev.yml run django /bin/sh -c "python manage.py test"