@echo off
echo == Updating database
for /f "delims=" %%i in ('docker-compose -f bin/docker/docker-compose.dev.yml ps --services --filter "status=running"') do set RUNNING=%%i
IF "%RUNNING%" == "" echo "ERROR: Before executing bin/update.bat, start server with bin/start.bat"
IF "%RUNNING%" == "" exit 1
docker-compose -f bin/docker/docker-compose.dev.yml exec django /bin/sh -c "cp bin/docker/entrypoint.sh bin/docker/win-entrypoint.sh"
docker-compose -f bin/docker/docker-compose.dev.yml exec django /bin/sh -c "sed -i 's/\r$//g' bin/docker/win-entrypoint.sh"
docker-compose -f bin/docker/docker-compose.dev.yml exec django /bin/sh -c "bin/docker/win-entrypoint.sh"
docker-compose -f bin/docker/docker-compose.dev.yml exec django /bin/sh -c "rm bin/docker/win-entrypoint.sh"