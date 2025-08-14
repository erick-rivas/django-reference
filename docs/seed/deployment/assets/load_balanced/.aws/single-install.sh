#!/bin/bash
# Install general dependencies for project

cd /home/ubuntu/<PROJECT>/

# General dependencies
sudo apt update
sudo apt install -y cloud-utils gettext postgresql-client software-properties-common curl git-core zlib1g-dev build-essential libssl-dev libreadline-dev libyaml-dev libsqlite3-dev sqlite3 libxml2-dev libxslt1-dev libcurl4-openssl-dev software-properties-common libffi-dev yarn

# Install python tools
sudo apt update
sudo apt install -y python3-pip python3-dev python3-venv libpq-dev nginx nginx-extras

# Install supervisor
sudo apt install -y supervisor

# Setup python environment
echo "== Creating virtual environment"
python3 -m venv .venv
cd /home/ubuntu/<PROJECT>/
. .venv/bin/activate

echo "== Installing dependencies"
python3 -m pip install --upgrade pip

chmod 777 /home/ubuntu/<PROJECT>/requirements.sh
/home/ubuntu/<PROJECT>/requirements.sh