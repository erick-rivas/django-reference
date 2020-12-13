# Django API - Deployment

This file contains guides to deploy project to aws elastic beanstalk

## Elastic beanstalk instance

-   Open aws console in [aws.amazon.com](https://aws.amazon.com),
-   Go to Elastic Beanstalk pane.
-   Create a new application.
-   Create a new environment (Web server environment)
    -   Select python platform **Amazon Linux**
    -   Press *Configure more options* 
        -   Go to Software and verify that Apache is set as server proxy
            >   If there are not options it is set by default
        -   Go to Database and create a new postgresql
        -   Go to Capacity and select the server capacity
            >   For development(sandbox) use preferably a t3a.nano instance
   
## EB command line interface

-   Install eb cli [See documentation](https://docs.aws.amazon.com/es_es/elasticbeanstalk/latest/dg/eb-cli3-install.html).
-   Configure AMI credentials [See documentation](https://docs.aws.amazon.com/es_es/general/latest/gr/managing-aws-access-keys.html).

## Pre-configuration

-   Create and configure *.env.prod* file.
-   Create a *.ebextensions* folder in root and copy inside
    -   [bin/aws-eb/config/apache-settings.config](./config/apache-settings.config)
    -   [bin/aws-eb/config/db.config](./config/db.config)
    -   [bin/aws-eb/config/django.config](./config/django.config)
-   Copy [bin/aws-eb/config/.ebignore](./config/.ebignore) to root folder

## Deployment

-   Run script
```bash
python3 manage.py collectstatic
eb deploy
```

## SSL settings

-   To enable ssl protocols (https) see [deployment-ssl.md](deployment-ssl.md).

## References
-   AWS reference [https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create-deploy-python-django.html](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create-deploy-python-django.html)
-   Python reference: [https://realpython.com/deploying-a-django-app-and-postgresql-to-aws-elastic-beanstalk/](https://realpython.com/deploying-a-django-app-and-postgresql-to-aws-elastic-beanstalk/)