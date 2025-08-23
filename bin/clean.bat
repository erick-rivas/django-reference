@echo off
:: Seed builder
:: AUTO_GENERATED (Read only)
:: Use $ bin/clean.bat <cleaning_type docker|files>

for /f "delims=" %%i in ('docker compose ps --services --filter "status=running"') do set RUNNING=%%i
IF "%RUNNING%" == "" (
  echo ERROR: Before executing bin/console.bat, start server with bin/start.bat
  exit 1
)

set CLEANING_TYPE=""
IF NOT "%~1" == "" set CLEANING_TYPE=%1

IF "%CLEANING_TYPE%" == "" (
 echo ERROR: Invalid option, use bin/clean.bat <docker|files>
 exit 1
)

IF "%CLEANING_TYPE%" == "docker" (
  echo == Cleaning unused docker resources
  docker image prune --force
  docker volume prune --force
)

IF "%CLEANING_TYPE%" == "files" (
  echo == Cleaning unused files
  docker compose exec django /bin/sh -c "python ./bin/scripts/clean_files.py"
)

echo == NOTICE: Run with administrative permissions
powershell -Command "& {Optimize-VHD -Path %LOCALAPPDATA%\Docker\wsl\data\ext4.vhdx -Mode Full}"