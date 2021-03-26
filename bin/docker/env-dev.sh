#!/bin/sh
echo "== Creating & configuring env.dev file"
cp .env.example .env.dev
sed -i "s/DB_NAME=/DB_NAME=postgres/" ".env.dev"
sed -i "s/DB_USER=/DB_USER=postgres/" ".env.dev"
sed -i "s/DB_PASSWORD=/DB_PASSWORD=postgres/" ".env.dev"
sed -i "s/DB_HOST=/DB_HOST=postgres/" ".env.dev"