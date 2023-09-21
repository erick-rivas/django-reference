@echo off
::: __Seed builder__
:: AUTO_GENERATED
:: Add custom commands at the end

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
del .env
echo # DOCKER SETTINGS > .\.env
echo ### MODIFY WITH WITH $ bin/setup.bat DJANGO_PORT POSTGRES_PORT REDIS_PORT IS_PROD ### >> .\.env
echo.>> .env
echo COMPOSE_PROJECT_NAME=django_reference_backend>> .\.env
echo COMPOSE_DJANGO_PORT=%DJANGO_PORT%>> .\.env
echo COMPOSE_POSTGRES_PORT=%POSTGRES_PORT%>> .\.env
echo COMPOSE_REDIS_PORT=%REDIS_PORT%>> .\.env
echo IS_PROD=%IS_PROD%>> .\.env

IF NOT EXIST .\debug_.py (
    echo # Temporary file for debugging, run with bin/debug.bat > .\debug_.py
)

echo == Deleting previous containers
docker compose down

echo == Building project
docker compose build

echo == Setting execute permissions to bin
docker compose run --rm django /bin/sh -c "chmod +x bin/*.sh;chmod +x bin/scripts/*.sh"

echo == Initializing .envs
docker compose run --rm django /bin/sh -c "cp bin/scripts/init_envs.sh bin/scripts/win_init_envs.sh"
docker compose run --rm django /bin/sh -c "sed -i 's/\r$//g' bin/scripts/win_init_envs.sh"
docker compose run --rm django /bin/sh -c "bin/scripts/win_init_envs.sh %POSTGRES_PORT% %REDIS_PORT% %SERVER_URL% %CLIENT_URL% %IS_PROD%"

echo == Starting services
docker compose up -d

echo == Executing db setup (make & run migrations)
docker compose exec django /bin/sh -c "python manage.py makemigrations"
docker compose exec django /bin/sh -c "python manage.py migrate"
docker compose exec django /bin/sh -c "python manage.py loaddata models/fixtures/*.yaml"

echo == Loading base fixtures (admin)
docker compose exec django /bin/sh -c "python manage.py loaddata models/fixtures/.base.yaml"

echo == Installing local dependencies
IF NOT EXIST .\.venv (
    python -m venv .venv
)
call ".\.venv\Scripts\activate"
python -m pip install --upgrade pip
python -m pip install -r requirements.txt

IF "%IS_PROD%" == "true" (
    echo == Exporting prod statics
    docker compose exec django /bin/sh -c "python manage.py collectstatic"
)

echo == Cleaning setup
docker compose exec django /bin/sh -c "rm bin/scripts/win_init_envs.sh"
docker compose stop
docker image prune --force
docker volume prune --force

echo.
echo == Setup completed (Start server with bin/start.bat)
echo.

IF "%IS_PROD%" == "true" (
    echo ***
    echo *** IMPORTANT: FOR SECURITY, CHANGE THE ADMIN PASSWORD IMMEDIATELY
    echo ***
    echo.
)

::  __End autogenerated__
::  Include commands after this block
:::