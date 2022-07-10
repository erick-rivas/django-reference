@echo off
:: Seed builder
:: AUTO_GENERATED (Read only)

for /f "delims=" %%i in ('docker compose -f bin/docker/docker-compose.yml ps --services --filter "status=running"') do set RUNNING=%%i
IF "%RUNNING%" == "" echo ERROR: Before executing bin/update.bat, start server with bin/start.bat
IF "%RUNNING%" == "" exit 1

echo == Updating database
docker compose -f bin/docker/docker-compose.yml exec django /bin/sh -c "cp bin/docker/update.sh bin/docker/win-update.sh"
docker compose -f bin/docker/docker-compose.yml exec django /bin/sh -c "sed -i 's/\r$//g' bin/docker/win-update.sh"
docker compose -f bin/docker/docker-compose.yml exec django /bin/sh -c "bin/docker/win-update.sh"
docker compose -f bin/docker/docker-compose.yml exec django /bin/sh -c "rm bin/docker/win-update.sh"