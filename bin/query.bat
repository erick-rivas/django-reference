@echo off
:: Seed builder
:: AUTO_GENERATED (Read only)

for /f "delims=" %%i in ('docker compose -f bin/docker/docker-compose.yml ps --services --filter "status=running"') do set RUNNING=%%i
IF "%RUNNING%" == "" echo ERROR: Before executing bin/query.bat, start server with bin/start.bat
IF "%RUNNING%" == "" exit 1

echo == Opening psql console
docker compose -f bin/docker/docker-compose.yml exec django /bin/sh -c "python manage.py dbshell"