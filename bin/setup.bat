@echo off
:: Seed builder
:: AUTO_GENERATED (Read only)

echo == Configuring docker .env
set /A DJANGO_PORT=8008
set /A POSTGRES_PORT=5435
set /A REDIS_PORT=6377
set SERVER_URL=http://localhost:8008
set CLIENT_URL=http://localhost:3003
set IS_PROD=false

IF NOT "%~1" == "" set /A DJANGO_PORT=%1
IF NOT "%~2" == "" set /A POSTGRES_PORT=%2
IF NOT "%~3" == "" set /A REDIS_PORT=%3
IF NOT "%~4" == "" set SERVER_URL=%4
IF NOT "%~5" == "" set CLIENT_URL=%5
IF NOT "%~6" == "" set IS_PROD=%6

echo == Creating docker .envs
del .\bin\docker\.env
echo # DOCKER PORTS > .\bin\docker\.env
echo ### MODIFY WITH WITH $ bin/setup.bat DJANGO_PORT POSTGRES_PORT REDIS_PORT IS_PROD ### >> .\bin\docker\.env
echo _ >> .\bin\docker\.env
echo COMPOSE_PROJECT_NAME=django_reference_backend >> .\bin\docker\.env
echo DJANGO_PORT=%DJANGO_PORT% >> .\bin\docker\.env
echo POSTGRES_PORT=%POSTGRES_PORT% >> .\bin\docker\.env
echo REDIS_PORT=%REDIS_PORT% >> .\bin\docker\.env

del .\bin\docker\.port
echo %DJANGO_PORT% > .\bin\docker\.port

del .\bin\docker\docker.env
echo IS_PROD=%IS_PROD%  > .\bin\docker\docker.env

IF NOT EXIST .\debug_.py (
    echo # Temporary file for debugging, run with bin/debug.bat > .\debug_.py
)

echo == Deleting previous containers
docker compose -f bin/docker/docker-compose.yml down

echo == Building project
docker compose -f bin/docker/docker-compose.yml build

echo == Setting execute permissions to bin
docker compose -f bin/docker/docker-compose.yml run --rm django /bin/sh -c "chmod +x bin/*.sh;chmod +x bin/docker/*.sh;chmod +x bin/scripts/*.sh"

echo == Initializing .env.devs
docker compose -f bin/docker/docker-compose.yml run --rm django /bin/sh -c "cp bin/scripts/init_envs.sh bin/scripts/win_init_envs.sh"
docker compose -f bin/docker/docker-compose.yml run --rm django /bin/sh -c "sed -i 's/\r$//g' bin/scripts/win_init_envs.sh"
docker compose -f bin/docker/docker-compose.yml run --rm django /bin/sh -c "bin/scripts/win_init_envs.sh %DJANGO_PORT% %POSTGRES_PORT% %REDIS_PORT% %SERVER_URL% %CLIENT_URL%"

echo == Starting services
docker compose -f bin/docker/docker-compose.yml up -d

echo == Executing db setup (make & run migrations)
docker compose -f bin/docker/docker-compose.yml exec django /bin/sh -c "python manage.py makemigrations"
docker compose -f bin/docker/docker-compose.yml exec django /bin/sh -c "python manage.py migrate"
docker compose -f bin/docker/docker-compose.yml exec django /bin/sh -c "python manage.py loaddata models/fixtures/*.yaml"

IF "%IS_PROD%" == "false" (
    echo == Loading dev fixtures (admin)
    docker compose -f bin/docker/docker-compose.yml exec django /bin/sh -c "python manage.py loaddata models/fixtures/.dev.yaml"
)

echo == Installing local dependencies
python -m venv .venv
call ".\.venv\Scripts\activate"
python -m pip install --upgrade pip
python -m pip install -r requirements.txt

echo == Cleaning setup
docker compose -f bin/docker/docker-compose.yml exec django /bin/sh -c "rm bin/scripts/win_init_envs.sh"

echo == Cleaning services
docker compose -f bin/docker/docker-compose.yml stop

echo.
echo == Setup completed (Start server with bin/start.bat)
echo.