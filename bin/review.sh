#!/bin/bash
# Seed builder
# AUTO_GENERATED (Read only)

echo "== Reviewing with pylint"
sudo codacy-analysis-cli analyze --tool pylint --force-file-permissions --parallel 4
echo "== Reviewing with bandit"
sudo codacy-analysis-cli analyze --tool bandit --force-file-permissions --parallel 4