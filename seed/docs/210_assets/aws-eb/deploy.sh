#!/bin/sh
# shellcheck disable=SC1090
. "$(pwd)"/.venv/bin/activate
python3 manage.py collectstatic
eb deploy