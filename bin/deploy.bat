@echo off
# Seed builder
# AUTO_GENERATED (Read only)

set /A KEY=0
set /A HOST=dev.seed-project.com.mx

IF NOT "%~1" == "" set KEY=%1
IF "%~1" == "" echo ERROR: Include deploy key-port e.g $ bin/deploy.sh 10120
IF "%~1" == "" exit 1
IF NOT "%~2" == "" set HOST=%2

echo "== Configuring variables"
for /f "delims=" %%i in ('git config --get remote.origin.url') do set git_url=%%i
for /f "delims=" %%i in ('git branch --show-current') do set git_branch=%%i
for /f "delims=" %%i in ('python -c "print(%KEY% + 0)') do set client_port=%%i
for /f "delims=" %%i in ('python -c "print(%KEY% + 1)') do set django_port=%%i
for /f "delims=" %%i in ('python -c "print(%KEY% + 2)') do set postgres_port=%%i
for /f "delims=" %%i in ('python -c "print(%KEY% + 3)') do set redis_port=%%i
set /A server_url="http://%HOST%:%django_port%"
set /A client_url="http://%HOST%:%client_port%"

echo == NOTE: BEFORE START paste .dev.pem in root dir

echo == Updating project
ssh -t -i .dev.pem ubuntu@%HOST% "git clone %git_url% %KEY%"
ssh -t -i .dev.pem ubuntu@%HOST% "cd %KEY%;git checkout %git_branch%"
ssh -t -i .dev.pem ubuntu@%HOST% "cd %KEY%;git pull"

echo == Updating django server
ssh -t -i .dev.pem ubuntu@%HOST% "cd %KEY%;bin/setup.sh %django_port% %postgres_port% %redis_port% %server_url% %client_url%"
ssh -t -i .dev.pem ubuntu@%HOST% "cd %KEY%;bin/start.sh"