@echo off
echo == Opening psql console
for /f "delims=" %%i in ('docker-compose -f bin/docker/docker-compose.dev.yml ps --services --filter "status=running"') do set RUNNING=%%i
IF "%RUNNING%" == "" echo "ERROR: Before executing bin/query.bat, start server with bin/start.bat"
IF "%RUNNING%" == "" exit 1
docker-compose -f bin/docker/docker-compose.dev.yml exec django /bin/sh -c "python manage.py dbshell"