# Django API - Deployment Ubuntu

This file contains guides to deploy project to a Debian Server (Ubuntu Server)

### Server installation

-   To install server dependencies, see [deployment-server.md](./deployment-server.md).

### Project installation

- Connect to server
```bash
ssh #USER@SERVER_URL#
```

-   To install project see [README#installation](../../README.md#installation)

### Project update

- Connect to server
```bash
ssh #USER@SERVER_URL#
```

-   Update project
```bash
cd #PROJECT_WEB_PATH#
sudo git pull origin dev
pip3 install -r requirements.txt
python3 manage.py migrate
python3 manage.py loaddata models/fixtures/*.yaml
python3 manage.py collectstatic
```

-   Restart server
```bash
sudo systemctl restart gunicorn
sudo systemctl restart nginx
```
-   For easily deployment paste [config.deploy.sh](./config/deploy.sh) in server root