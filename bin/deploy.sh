#!/bin/bash
# Seed builder
# AUTO_GENERATED (Read only)

KEY=0
HOST="dev.seed-project.com.mx"

if [ $# -ge 1 ]; then
  KEY=$1;
else
  echo "ERROR: Include deploy key (port) e.g $ bin/deploy.sh 10120"
  exit 1
fi
if [ $# -ge 2 ]; then HOST=$2; fi

echo "== Configuring variables"
git_url=$(git config --get remote.origin.url)
git_branch=$(git branch --show-current)
client_port=$(python3 -c "print($KEY + 0)")
django_port=$(python3 -c "print($KEY + 1)")
postgres_port=$(python3 -c "print($KEY + 2)")
redis_port=$(python3 -c "print($KEY + 3)")
server_url="http://$HOST:$django_port"
client_url="http://$HOST:$client_port"

echo "== NOTE: BEFORE START paste .dev.pem in root dir"
sudo chmod 400 .dev.pem

echo "== Updating project"
ssh -t -i .dev.pem ubuntu@$HOST "git clone $git_url $KEY"
ssh -t -i .dev.pem ubuntu@$HOST "cd $KEY;git checkout $git_branch"
ssh -t -i .dev.pem ubuntu@$HOST "cd $KEY;git pull"

echo "== Updating django server"
ssh -t -i .dev.pem ubuntu@$HOST "cd $KEY;bin/setup.sh $django_port $postgres_port $redis_port $server_url $client_url"
ssh -t -i .dev.pem ubuntu@$HOST "cd $KEY;bin/start.sh"