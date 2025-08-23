@echo off
:: Seed builder
:: AUTO_GENERATED (Read only)
:: Use $ bin/migrate.bat

for /f "delims=" %%i in ('docker compose ps --services --filter "status=running"') do set RUNNING=%%i
IF "%RUNNING%" == "" (
  echo ERROR: Before executing bin/console.bat, start server with bin/start.bat
  exit 1
)

echo == Migrating database
docker compose exec django /bin/sh -c "python manage.py makemigrations"
docker compose exec django /bin/sh -c "python manage.py migrate"