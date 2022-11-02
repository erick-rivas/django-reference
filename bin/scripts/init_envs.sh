#!/bin/sh
# Seed builder
# AUTO_GENERATED (Read only)

DJANGO_PORT=$1
POSTGRES_PORT=$2
REDIS_PORT=$3
SERVER_URL=${4//[\/]/\\\/}
CLIENT_URL=${5//[\/]/\\\/}

if [ ! -f .env.docker.dev ]; then
    echo "== Creating & configuring env.docker.dev file"
    cp .env.example .env.docker.dev
    sed -i "s/SERVER_URL=http:\/\/localhost:8000/SERVER_URL=$SERVER_URL/" ".env.docker.dev"
    sed -i "s/CLIENT_URL=http:\/\/localhost:3000/CLIENT_URL=$CLIENT_URL/" ".env.docker.dev"
    sed -i "s/DB_NAME=/DB_NAME=postgres/" ".env.docker.dev"
    sed -i "s/DB_USER=/DB_USER=postgres/" ".env.docker.dev"
    sed -i "s/DB_PASSWORD=/DB_PASSWORD=postgres/" ".env.docker.dev"
    sed -i "s/DB_HOST=/DB_HOST=postgres/" ".env.docker.dev"
    sed -i "s/REDIS_HOST=/REDIS_HOST=redis/" ".env.docker.dev"
    sed -i "s/SECRET_KEY=/SECRET_KEY=fupswltefA9efredrufihUSTOwamc/" ".env.docker.dev"
fi

if [ ! -f .env.dev ]; then
    echo "== Creating & configuring env.dev file"
    cp .env.example .env.dev
    sed -i "s/CLIENT_URL=http:\/\/localhost:3000/CLIENT_URL=$CLIENT_URL/" ".env.dev"
    sed -i "s/DB_NAME=/DB_NAME=postgres/" ".env.dev"
    sed -i "s/DB_USER=/DB_USER=postgres/" ".env.dev"
    sed -i "s/DB_PASSWORD=/DB_PASSWORD=postgres/" ".env.dev"
    sed -i "s/DB_HOST=/DB_HOST=localhost/" ".env.dev"
    sed -i "s/DB_PORT=5432/DB_PORT=$POSTGRES_PORT/" ".env.dev"
    sed -i "s/REDIS_HOST=/REDIS_HOST=localhost/" ".env.dev"
    sed -i "s/REDIS_PORT=6379/REDIS_PORT=$REDIS_PORT/" ".env.dev"
    sed -i "s/SECRET_KEY=/SECRET_KEY=fupswltefA9efredrufihUSTOwamc/" ".env.dev"
fi