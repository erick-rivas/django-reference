@echo off
echo == Updating database
docker-compose -f bin/docker/docker-compose.dev.yml run django /bin/sh -c "cp bin/docker/entrypoint.sh bin/docker/win-entrypoint.sh"
docker-compose -f bin/docker/docker-compose.dev.yml run django /bin/sh -c "sed -i 's/\r$//g' bin/docker/win-entrypoint.sh"
docker-compose -f bin/docker/docker-compose.dev.yml run django /bin/sh -c "bin/docker/win-entrypoint.sh"
docker-compose -f bin/docker/docker-compose.dev.yml run django /bin/sh -c "rm bin/docker/win-entrypoint.sh"