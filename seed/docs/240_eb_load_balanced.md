## AWS-EB load-balanced

### Elastic beanstalk instance

-   Open aws console in [aws.amazon.com](https://aws.amazon.com),
-   Go to Elastic Beanstalk pane.
-   Create a new application.
-   Create a new environment (Web server environment)
    -   Select python platform **Amazon Linux**
    -   Press *Configure more options* 
        -   Go to Database and create a new postgresql db
        -   Go to Capacity, capacity type and select load balanced as Environment type
        
### EB command line interface

-   Install eb cli [See documentation](https://docs.aws.amazon.com/es_es/elasticbeanstalk/latest/dg/eb-cli3-install.html).
-   Configure AMI credentials [See documentation](https://docs.aws.amazon.com/es_es/general/latest/gr/managing-aws-access-keys.html).

### Pre-configuration

-   Create and configure *.env.prod* file.
-   Create a `.ebextensions` folder in the root directory of the project and copy inside
    -   `seed/docs/210_assets/aws-eb/load-balanced/apache-settings.config`
    -   `seed/docs/210_assets/aws-eb/load-balanced/db.config`
    -   `seed/docs/210_assets/aws-eb/load-balanced/django.config`
-   Copy `seed/docs/210_assets/aws-eb/load-balanced/.ebignore` in the root directory of the project
-   Copy `seed/docs/210_assets/aws-eb/load-balanced/deploy.sh` in `/bin` folder

### SSL

To enable a https connection

#### Create an AWS certificate

-   Go to AWS Certificate Manager
-   Create a new public certificate
-   Press option "Export DNS configuration to a file" and place those record in a new CNAME record in order to validate certificate

#### Open 443 port 

-   Enable 443 port in ec2 settings
    -   Go to ec2 pane 
    -   Press security groups
    -   Find security group with environment name
    -   Go to inbound
    -   Enable 443 port

#### Assign certificate

-    Go to aws eb config and press edit in the load balancer section
-    Add a new listener to 443 port with a https protocol 
    -   Select the SSL certificate created in AWS Certificate Manager
    -   In SSL policies, use ELBSecurityPolicy-FS-1-2-2019-08

#### Enable application settings

-    Copy `seed/docs/210_assets/aws-eb/https-reencrypt-alb.config` into `.ebextensions` folder

### Deployment

-   Run script `./seed/docs/210_assets/aws-eb/deploy.sh`

### References
-   AWS reference [https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create-deploy-python-django.html](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create-deploy-python-django.html)
-   Python reference: [https://realpython.com/deploying-a-django-app-and-postgresql-to-aws-elastic-beanstalk/](https://realpython.com/deploying-a-django-app-and-postgresql-to-aws-elastic-beanstalk/)