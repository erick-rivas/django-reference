PWD=`pwd`
activate () {
    . $PWD/.venv/bin/activate
}
activate

echo "== Making & executing migrations"
python3 manage.py makemigrations
python3 manage.py migrate

echo "== Filling database"
python3 manage.py loaddata models/fixtures/*.yaml

echo "== Creating documentation"
chmod 777 ./bin/docs.sh
./bin/docs.sh