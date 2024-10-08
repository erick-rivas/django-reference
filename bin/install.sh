#!/bin/bash
### __Seed builder__
# AUTO_GENERATED
# Add custom commands at the end

RUNNING=$(sudo docker compose ps --services --filter "status=running")
if [ $RUNNING -z ]; then
  echo "ERROR: Before executing bin/install.sh, start server with bin/start.sh"
  exit 1
fi

echo "== Installing dependencies"
sudo docker compose exec django /bin/sh -c "pip install -r requirements.txt --no-cache-dir"

echo "== Installing local dependencies"
if [ ! -d .venv ]; then
  python3 -m venv .venv
fi
. "$(pwd)"/.venv/bin/activate
python3 -m pip install --upgrade pip
pip3 install -r requirements.txt

#  __End autogenerated__
#  Include commands after this block
###