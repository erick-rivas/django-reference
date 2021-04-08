@echo off

echo == Configuring docker .env
set /A DJANGO_PORT=8008
set /A POSTGRES_PORT=5435
set /A REDIS_PORT=6377

IF NOT "%~1" == "" set DJANGO_PORT=%1
IF NOT "%~2" == "" set POSTGRES_PORT=%2
IF NOT "%~3" == "" set REDIS_PORT=%3

del .\bin\docker\.env
echo # DOCKER PORTS > .\bin\docker\.env
echo ### MODIFY WITH WITH $ bin/setup.bat DJANGO_PORT POSTGRES_PORT REDIS_PORT ### >> .\bin\docker\.env
echo _ >> .\bin\docker\.env
echo DJANGO_PORT=%DJANGO_PORT% >> .\bin\docker\.env
echo POSTGRES_PORT=%POSTGRES_PORT% >> .\bin\docker\.env
echo REDIS_PORT=%REDIS_PORT% >> .\bin\docker\.env

echo == Deleting previous containers
docker-compose -f bin/docker/docker-compose.dev.yml down

echo == Building project
docker-compose -f bin/docker/docker-compose.dev.yml build

echo == Setting execute permissions to bin and fix unix linebreaks
docker-compose -f bin/docker/docker-compose.dev.yml run django /bin/sh -c "chmod +x bin/*;chmod +x bin/docker/*"
docker-compose -f bin/docker/docker-compose.dev.yml run django /bin/sh -c "sed -i 's/\r$//g' bin/docker/env-dev.sh"
docker-compose -f bin/docker/docker-compose.dev.yml run django /bin/sh -c "sed -i 's/\r$//g' bin/docker/entrypoint.sh"

echo == Creating .env.devs
docker-compose -f bin/docker/docker-compose.dev.yml run django /bin/sh -c "bin/docker/env-dev.sh"

echo == Executing entrypoint.sh (make & run migrations)
docker-compose -f bin/docker/docker-compose.dev.yml run django /bin/sh -c "bin/docker/entrypoint.sh"

echo == Loading dev fixtures (admin)
docker-compose -f bin/docker/docker-compose.dev.yml run django /bin/sh -c "python manage.py loaddata bin/docker/fixtures-dev.yaml"

echo == Generating docs
docker-compose -f bin/docker/docker-compose.dev.yml run django /bin/sh -c "sphinx-build -E -b html ./docs ./.data/docs"