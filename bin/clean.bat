@echo off
:: Seed builder
:: AUTO_GENERATED (Read only)

set CLEAN_FILES=false

IF NOT "%~1" == "" set CLEAN_FILES=%1

echo == Cleaning unused docker resources
docker image prune --force
docker volume prune --force

IF "%CLEAN_FILES%" == "true" (
  echo == Cleaning unused files
  docker compose exec django /bin/sh -c "python ./bin/scripts/clean_files.py"
)

echo == NOTICE: Run with administrative permissions
powershell -Command "& {Optimize-VHD -Path %LOCALAPPDATA%\Docker\wsl\data\ext4.vhdx -Mode Full}"