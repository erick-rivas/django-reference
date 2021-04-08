@echo off
echo == Analyzing with pylint
docker-compose -f bin/docker/docker-compose.dev.yml run codacy-cli analyze --tool pylint --force-file-permissions
echo == Analyzing with bandit
docker-compose -f bin/docker/docker-compose.dev.yml run codacy-cli analyze --tool bandit --force-file-permissions