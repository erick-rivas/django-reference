#!/bin/bash
echo "== Analyzing with pylint"
codacy-analysis-cli analyze --tool pylint --force-file-permissions
echo "== Analyzing with bandit"
codacy-analysis-cli analyze --tool bandit --force-file-permissions