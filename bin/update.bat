@echo off
echo == Updating database
docker-compose -f bin/docker/docker-compose.dev.yml run django /bin/sh -c "bin/docker/entrypoint.sh"