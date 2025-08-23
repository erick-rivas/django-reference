@echo off
:: Seed builder
:: AUTO_GENERATED (Read only)
:: Use $ bin/review.bat

echo == Reviewing with pylint
codacy-analysis-cli analyze --tool pylint --force-file-permissions --parallel 4
echo == Reviewing with bandit
codacy-analysis-cli analyze --tool bandit --force-file-permissions --parallel 4
echo == Reviewing with pmd
codacy-analysis-cli analyze --tool pmd --force-file-permissions --parallel 4