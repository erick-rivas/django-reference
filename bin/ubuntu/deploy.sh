# Connect to server

ssh <SERVER_URL>

# Update project

cd <PROJECT_WEB_PATH>
sudo git pull origin dev
python3 manage.py migrate
python3 manage.py loaddata fixtures/*.yaml

# Restart server

sudo systemctl restart gunicorn
sudo systemctl restart nginx
