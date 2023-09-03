## Ubuntu Server - 22.04

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

#### Deploy on reboot

-   Copy `seed/docs/assets/ubuntu/reboot.sh` in project root folder
-   Execute `crontab -e`
-   Include `@reboot <root_path>/reboot.sh`
    -   Example `/home/ubuntu/reboot.sh`

### Server configuration files

-   To open gunicorn configuration files `sudo vim /etc/systemd/system/gunicorn.service`
    -   To update files
    ```
    sudo systemctl start gunicorn.socket
    sudo systemctl enable gunicorn.socket
    sudo systemctl restart gunicorn
    sudo systemctl status gunicorn --no-pager
    ```

-   To open nginx configuration files `sudo vim /etc/nginx/sites-available/app`
    -   To update files
    ```
    sudo nginx -t
    sudo systemctl restart nginx
    ```

### Server logs

-   To watch gunicorn logs (main) `tail -f /var/log/gunicorn.access.log`
-   To watch nginx logs `tail -f /var/log/nginx/access.log` or `tail -f /var/log/nginx/error.log`

### References

-   Gunicorn-nginx tutorial [https://www.digitalocean.com/community/tutorials/how-to-set-up-django-with-postgres-nginx-and-gunicorn-on-ubuntu-18-04#creating-systemd-socket-and-service-files-for-gunicorn](https://www.digitalocean.com/community/tutorials/how-to-set-up-django-with-postgres-nginx-and-gunicorn-on-ubuntu-18-04#creating-systemd-socket-and-service-files-for-gunicorn)
-   PostgreSQL SSL [https://www.vultr.com/docs/use-ssl-encryption-with-postgresql-on-ubuntu-20-04/](https://www.vultr.com/docs/use-ssl-encryption-with-postgresql-on-ubuntu-20-04/)
-   Increase storage EC2 [https://medium.com/@m.yunan.helmy/increase-the-size-of-ebs-volume-in-your-ec2-instance-3859e4be6cb7] (https://medium.com/@m.yunan.helmy/increase-the-size-of-ebs-volume-in-your-ec2-instance-3859e4be6cb7)

### See also

-   [Ubuntu extras](./extras/211_deploy_ubuntu_extras.md)