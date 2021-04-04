#!/bin/sh
PWD=`pwd`
. $PWD/.venv/bin/activate
python3 manage.py collectstatic
eb deploy