@echo off
::: __Seed builder__
:: AUTO_GENERATED
:: Add custom commands at the end

for /f "delims=" %%i in ('docker compose ps --services --filter "status=running"') do set RUNNING=%%i
IF "%RUNNING%" == "" echo ERROR: Before executing bin/install.bat, start server with bin/start.bat
IF "%RUNNING%" == "" exit 1

echo == Installing dependencies
docker compose exec django /bin/sh -c "pip install -r requirements.txt --no-cache-dir"

echo == Installing local dependencies
IF NOT EXIST .\.venv (
  python -m venv .venv
)
call ".\.venv\Scripts\activate"
python -m pip install --upgrade pip
python -m pip install -r requirements.txt

::  __End autogenerated__
::  Include commands after this block
:::