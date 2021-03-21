PWD=`pwd`
activate () {
    . $PWD/.venv/bin/activate
}
activate
python3 manage.py collectstatic
eb deploy