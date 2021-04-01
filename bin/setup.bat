# Configure docker .env
@echo off
del ./.env
echo "# DOCKER PORTS (DON'T MODIFY)" > ".env"
echo "DJANGO_PORT=8008" >> ".env"
echo "POSTGRES_PORT=5435" >> ".env"
echo "REDIS_PORT=6377" >> ".env"

# Configure docker .env
cp ./bin/docker/.docker.env ./.env

# Delete previous containers
docker-compose -f bin/docker/docker-compose.dev.yml down

# Build project
docker-compose -f bin/docker/docker-compose.dev.yml build

# Set execute permissions to bin
docker-compose -f bin/docker/docker-compose.dev.yml run django chmod +x bin/*;chmod +x bin/docker/* 

# Creating .env.devs
docker-compose -f bin/docker/docker-compose.dev.yml run django bin/docker/env-dev.sh 8008 5435 6377

# Execute entrypoint.sh (make & run migrations)
docker-compose -f bin/docker/docker-compose.dev.yml run django bin/docker/entrypoint.sh

# Generate docs
docker-compose -f bin/docker/docker-compose.dev.yml run django sphinx-build -E -b html ./docs ./.data/docs

