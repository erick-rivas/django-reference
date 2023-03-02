## Ubuntu Server - 20.04

This file contains guides to deploy project to a (Ubuntu Server)

### Server installation

-   Clone repository
-   Execute installation script ```seed/docs/assets/ubuntu/install.sh #SERVER_NAME# #DB_NAME# #DB_USER# #DB_PASSWORD#```
    >  Example: ```seed/docs/assets/ubuntu/install.sh seed-project.com db admin 123```
-   In case of require ssl execute ```seed/docs/assets/ubuntu/install-ssl.sh #SERVER_NAME#```

### Project settings

-   Adjust .env.dev or .env.prod for production environment and adjust the project variables
```
# Important settings
SERVER_URL=#SERVER_URL#
CLIENT_URL=#CLIENT_URL#
SECRET_KEY=#ANY_SECRET_KEY#
ENABLE_AUTH=true/false
```
-   To update variables execute
```
sudo supervisorctl restart celery
sudo systemctl restart gunicorn
sudo systemctl restart nginx
```

#### Production environment

-  For  production set the environment variable IS_PROD=true
```bash
vim ~/.bash_profile
export IS_PROD=true
```

### ReactJS configuration (optional)

-   Check reference [documentation](https://github.com/erick-rivas/reactjs-reference/blob/master/src/seed/docs/220_ubuntu.md)

### Deployment

-   Copy `seed/docs/assets/ubuntu/deploy.sh` in project root folder
-   Modify deploy.sh settings
```
API_DIR="###"
WEB_DIR="###"
```

-   Run deployment script `deploy.sh`
    > For automatic deployment check [AW Code Deploy documentation](230_eb_single_instance.md)

### Server logs

-   To watch gunicorn logs (main) `tail -f /var/log/gunicorn.access.log`
-   To watch nginx logs `tail -f /var/log/nginx/access.log`

### References

-   Gunicorn-nginx tutorial [https://www.digitalocean.com/community/tutorials/how-to-set-up-django-with-postgres-nginx-and-gunicorn-on-ubuntu-18-04#creating-systemd-socket-and-service-files-for-gunicorn](https://www.digitalocean.com/community/tutorials/how-to-set-up-django-with-postgres-nginx-and-gunicorn-on-ubuntu-18-04#creating-systemd-socket-and-service-files-for-gunicorn)
-   PostgreSQL SSL [https://www.vultr.com/docs/use-ssl-encryption-with-postgresql-on-ubuntu-20-04/](https://www.vultr.com/docs/use-ssl-encryption-with-postgresql-on-ubuntu-20-04/)
-   Increase storage EC2 [https://medium.com/@m.yunan.helmy/increase-the-size-of-ebs-volume-in-your-ec2-instance-3859e4be6cb7] (https://medium.com/@m.yunan.helmy/increase-the-size-of-ebs-volume-in-your-ec2-instance-3859e4be6cb7)

### See also

-   [Ubuntu extras](221_ubuntu_extras.md)
-   [AWS Code Deploy](222_code_deploy.md)