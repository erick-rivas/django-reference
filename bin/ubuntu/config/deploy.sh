# Update project

cd <PROJECT_WEB_PATH>
sudo git pull origin dev
PWD=`pwd`
activate () {
    . $PWD/.venv/bin/activate
}
activate
pip3 install -r requirements.txt
python3 manage.py migrate
python3 manage.py loaddata fixtures/*.yaml
python3 manage.py collectstatic

# Restart server

sudo systemctl restart gunicorn
sudo systemctl restart nginx