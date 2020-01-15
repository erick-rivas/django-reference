# Django API - Deployment

This file contains guides to deploy project to aws elastic beanstalk

### Elastic beanstalk instance

-   Open aws console in [aws.amazon.com](https://aws.amazon.com),
-   Go to elastic beanstalk pane.
-   Create a new application (if required).
-   Create a new environment.
    -   Select python platform.
    -   Press *more_options* and go to database.
    -   Create a new **postgresql** database.
    >   For development(sandbox)  use preferably a t3a.nano instance
   
### EB CLI

-   Install eb terminal [Documentation](https://docs.aws.amazon.com/es_es/elasticbeanstalk/latest/dg/eb-cli3-install.html).
-   Create credentials [Documentation](https://docs.aws.amazon.com/es_es/general/latest/gr/managing-aws-access-keys.html).

### Security settings

-   To enable security protocols, see [deployment-security.md](./deployment-security.md).

### Production settings

-   Move bin/eb/.ebextensions & bin/eb/.ebignore to root folder
-   Create and configure *.env.prod* file.
-   Make database migrations.
```bash
(.venv)$ python3 manage.py makemigrations
```

### Deploy example

-   Run command to aws.
```bash
$ ./bin/deploy
```