#!/bin/bash
# Seed builder
# AUTO_GENERATED (Read only)

DJANGO_PORT=$1
POSTGRES_PORT=$2
REDIS_PORT=$3
SERVER_URL=${4//[\/]/\\\/}
CLIENT_URL=${5//[\/]/\\\/}
IS_PROD=$6

DOCKER_ENV=".env.docker.dev"
LOCAL_ENV=".env.dev"
if [ $IS_PROD = true ]; then
    DOCKER_ENV=".env.docker.prod"
    LOCAL_ENV=".env.prod"
fi

if [ ! -f $DOCKER_ENV ]; then
    echo "== Creating & configuring $DOCKER_ENV file"
    cp .env.example $DOCKER_ENV
    sed -i "s/SERVER_URL=http:\/\/localhost:8000/SERVER_URL='$SERVER_URL'/" "$DOCKER_ENV"
    sed -i "s/CLIENT_URL=http:\/\/localhost:3000/CLIENT_URL='$CLIENT_URL'/" "$DOCKER_ENV"
    sed -i "s/SERVER_URL='http:\/\/localhost:8000'/SERVER_URL='$SERVER_URL'/" "$DOCKER_ENV"
    sed -i "s/CLIENT_URL='http:\/\/localhost:3000'/CLIENT_URL='$CLIENT_URL'/" "$DOCKER_ENV"
    sed -i "s/DB_NAME=/DB_NAME='postgres'/" "$DOCKER_ENV"
    sed -i "s/DB_USER=/DB_USER='postgres'/" "$DOCKER_ENV"
    sed -i "s/DB_PASSWORD=/DB_PASSWORD='postgres'/" "$DOCKER_ENV"
    sed -i "s/DB_HOST=/DB_HOST='postgres'/" "$DOCKER_ENV"
    sed -i "s/REDIS_HOST=/REDIS_HOST='redis'/" "$DOCKER_ENV"
    sed -i "s/SECRET_KEY=/SECRET_KEY='fupswltefA9efredrufihUSTOwamc'/" "$DOCKER_ENV"
fi

if [ ! -f $LOCAL_ENV ]; then
    echo "== Creating & configuring $LOCAL_ENV file"
    cp .env.example $LOCAL_ENV
    sed -i "s/CLIENT_URL=http:\/\/localhost:3000/CLIENT_URL='$CLIENT_URL'/" "$LOCAL_ENV"
    sed -i "s/CLIENT_URL='http:\/\/localhost:3000'/CLIENT_URL='$CLIENT_URL'/" "$LOCAL_ENV"
    sed -i "s/DB_NAME=/DB_NAME='postgres'/" "$LOCAL_ENV"
    sed -i "s/DB_USER=/DB_USER='postgres'/" "$LOCAL_ENV"
    sed -i "s/DB_PASSWORD=/DB_PASSWORD='postgres'/" "$LOCAL_ENV"
    sed -i "s/DB_HOST=/DB_HOST='localhost'/" "$LOCAL_ENV"
    sed -i "s/DB_PORT=5432/DB_PORT=$POSTGRES_PORT/" "$LOCAL_ENV"
    sed -i "s/REDIS_HOST=/REDIS_HOST='localhost'/" "$LOCAL_ENV"
    sed -i "s/REDIS_PORT=6379/REDIS_PORT=$REDIS_PORT/" "$LOCAL_ENV"
    sed -i "s/SECRET_KEY=/SECRET_KEY='fupswltefA9efredrufihUSTOwamc'/" "$LOCAL_ENV"
fi