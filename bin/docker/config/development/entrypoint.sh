#!/bin/sh

if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $DB_HOST $DB_PORT; do
      sleep 5
    done

    echo "PostgreSQL started"
fi

# wait for Postgres to start
#function postgres_ready(){
#python << END
#import sys
#import psycopg2
#try:
#    conn = psycopg2.connect(dbname="postgres", user="postgres", password="postgres", host="postgres")
#    conn.close()
#except psycopg2.OperationalError:
#    sys.exit(-1)
#sys.exit(0)
#END
#}

#until postgres_ready; do
#  >&2 echo "Postgres is unavailable - sleeping"
#  sleep 10
#done

python manage.py flush --no-input
python manage.py makemigrations
python manage.py migrate

exec "$@"