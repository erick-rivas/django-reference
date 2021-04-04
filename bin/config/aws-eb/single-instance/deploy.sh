#!/bin/sh
PWD=`pwd`
# shellcheck disable=SC1090
. "$PWD"/.venv/bin/activate
python3 manage.py collectstatic
eb deploy