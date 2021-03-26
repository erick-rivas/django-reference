#!/bin/sh

echo "== Creating & configuring env.docker.dev file"
cp .env.example .env.docker.dev
sed -i "s/HOST_URL=http:\/\/localhost:8000/HOST_URL=http:\/\/localhost:8008/" ".env.docker.dev"
sed -i "s/DB_NAME=/DB_NAME=postgres/" ".env.docker.dev"
sed -i "s/DB_USER=/DB_USER=postgres/" ".env.docker.dev"
sed -i "s/DB_PASSWORD=/DB_PASSWORD=postgres/" ".env.docker.dev"
sed -i "s/DB_HOST=/DB_HOST=postgres/" ".env.docker.dev"

echo "== Creating & configuring env.dev file"
cp .env.example .env.dev
sed -i "s/DB_NAME=/DB_NAME=postgres/" ".env.dev"
sed -i "s/DB_USER=/DB_USER=postgres/" ".env.dev"
sed -i "s/DB_PASSWORD=/DB_PASSWORD=postgres/" ".env.dev"
sed -i "s/DB_HOST=/DB_HOST=localhost/" ".env.dev"
sed -i "s/DB_PORT=5432/DB_PORT=5435/" ".env.dev"