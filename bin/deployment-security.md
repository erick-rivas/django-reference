# Django API - Security

This file contains guides to enable security practices (hardware & deployment) for django api

## Limit anonymous users

To limit request to registered users (token authentication):

-  Add ENABLE_SECURITY=true to .env files

### Test token request

-  Generate temp token
```bash
(.venv)$ python3 manage.py drf_create_token 
```

-  Send a request with the authentication params
```bash
$ curl -i -X GET http://127.0.0.1:8000/api/players -H 'Authorization: Token '
```

## Https

To enable a https connection:

### Configure aws/dns settings

-  Create an elastic beanstalk instance for reactjs support (see [README.md](../README.md))   

-  Enable 443 port in ec2 settings
   -  Go to ec2 pane 
   -  Press instance name
   -  Open first security groups
   -  Go to inbound
   -  Enable 443 port

### Configure server

-  Install eb terminal and init project (see [README.md](../README.md))
-  Enable & execute ssh

```bash
$ eb ssh --setup
$ eb ssh
```

-  Setup apache settings

```bash
$ sudo vim /etc/httpd/conf.d/temp.conf
<VirtualHost *:80 *:443>
	ServerName <HTTPS_DOMAIN>
	DocumentRoot /var/www/html
</VirtualHost>
```

-  Install and configure certbot

```bash
$ sudo wget https://dl.eff.org/certbot-auto
$ sudo chmod a+x ./certbot-auto
$ sudo ./certbot-auto certonly --debug
  # Select 1. apache
```

-  Copy bin/eb/http-instance.config to .ebextensions folder
-  Set HTTPS_DOMAIN in .ebextensions/django.config