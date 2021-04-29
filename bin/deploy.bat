@echo off
# Seed builder
# AUTO_GENERATED (Read only)

set /A KEY=0
set /A HOST=dev.seed-project.com.mx

IF NOT "%~1" == "" set KEY=%1
IF "%~1" == "" echo ERROR: Include deploy port-key e.g $ bin/deploy.sh 7120
IF "%~1" == "" exit 1
IF NOT "%~2" == "" set HOST=%2
if %KEY lss 7000 OR $KEY gtr 7999 echo ERROR: Invalid port-key, valid range [7000-7999]
if %KEY lss 7000 OR $KEY gtr 7999 exit 1

echo "== Configuring variables"
for /f "delims=" %%i in ('git config --get remote.origin.url') do set git_url=%%i
for /f "delims=" %%i in ('git branch --show-current') do set git_branch=%%i
for /f "delims=" %%i in ('python -c "print(%KEY% + 0)"') do set client_port=%%i
for /f "delims=" %%i in ('python -c "print(%KEY% + 1)"') do set django_port=%%i
for /f "delims=" %%i in ('python -c "print(%KEY% + 2)"') do set postgres_port=%%i
for /f "delims=" %%i in ('python -c "print(%KEY% + 3)"') do set redis_port=%%i
set /A server_url="http://%HOST%:%django_port%"
set /A client_url="http://%HOST%:%client_port%"

echo == NOTE: BEFORE START paste .dev.pem in root dir

echo == Updating project
ssh -t -i .dev.pem ubuntu@%HOST% "git clone %git_url% %KEY%/api"
ssh -t -i .dev.pem ubuntu@%HOST% "cd %KEY%/api;git reset --hard"
ssh -t -i .dev.pem ubuntu@%HOST% "cd %KEY%/api;git clean -f -d"
ssh -t -i .dev.pem ubuntu@%HOST% "cd %KEY%/api;git checkout %git_branch%"
ssh -t -i .dev.pem ubuntu@%HOST% "cd %KEY%/api;git pull"

echo == Configuring docker
ssh -t -i .dev.pem ubuntu@%HOST% "cd %KEY%/api;sed -i \"s/run django/run django-%KEY%/\" \"bin/setup.sh\""
ssh -t -i .dev.pem ubuntu@%HOST% "cd %KEY%/api;sed -i \"s/exec django/exec django-%KEY%/\" \"bin/setup.sh\""
ssh -t -i .dev.pem ubuntu@%HOST% "cd %KEY%/api;sed -i \"s/ django:/ django-%KEY%:/\" \"bin/docker/docker-compose.dev.yml\""
ssh -t -i .dev.pem ubuntu@%HOST% "cd %KEY%/api;sed -i \"s/ postgres:/ postgres-%KEY%:/\" \"bin/docker/docker-compose.dev.yml\""
ssh -t -i .dev.pem ubuntu@%HOST% "cd %KEY%/api;sed -i \"s/ redis:/ redis-%KEY%:/\" \"bin/docker/docker-compose.dev.yml\""
ssh -t -i .dev.pem ubuntu@%HOST% "cd %KEY%/api;sed -i \"s/- postgres/- postgres-%KEY%/\" \"bin/docker/docker-compose.dev.yml\""
ssh -t -i .dev.pem ubuntu@%HOST% "cd %KEY%/api;sed -i \"s/- redis/- redis-%KEY%/\" \"bin/docker/docker-compose.dev.yml\""
ssh -t -i .dev.pem ubuntu@%HOST% "cd %KEY%/api;sed -i \"s/DB_HOST=postgres/DB_HOST=postgres-%KEY%/\" \"bin/docker/env-dev.sh\""
ssh -t -i .dev.pem ubuntu@%HOST% "cd %KEY%/api;sed -i \"s/REDIS_HOST=redis/REDIS_HOST=redis-%KEY%/\" \"bin/docker/env-dev.sh\""

echo == Updating django server
ssh -t -i .dev.pem ubuntu@%HOST% "cd %KEY%/api;bin/setup.sh %django_port% %postgres_port% %redis_port% %server_url% %client_url%"
ssh -t -i .dev.pem ubuntu@%HOST% "cd %KEY%/api;bin/start.sh"

echo.
echo == Deployment completed (http://%HOST%:%django_port%)
echo.