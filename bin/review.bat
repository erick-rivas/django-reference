@echo off
:: Seed builder
:: AUTO_GENERATED (Read only)

echo == Reviewing with pylint
codacy-analysis-cli analyze --tool pylint --force-file-permissions
echo == Reviewing with bandit
codacy-analysis-cli analyze --tool bandit --force-file-permissions