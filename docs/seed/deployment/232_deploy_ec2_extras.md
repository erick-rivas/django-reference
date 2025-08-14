## AWS EC2 (Extras)

### Migrate a domain from goddady to ROute53

#### From GoDaddy

* Go to Amazon Route53 service and create a hosted zone with your domain name. Then click on NS record and copy all of them. Looks like: ns-xxxx.awsdns-xx.org. ns-xxxx.awsdns-xx.co.uk. ns-xxx.awsdns-xx.com. ns-xxx.awsdns-xx.net.
* In GoDaddy, go to Nanage DNS in your domain and click in Change Nameservers button, select "Enter my own nameservers (advanced)" and paste all Route53 NS copied previously.

#### Manual subdomain

* Click on Create Record.
* Select Record Type (A for IPV4, AAAA for IPV6, CNAME for domains, etc.).
* In value, type ip or domain you want to redirect.

#### Automatic subdomain

Before this, it's required to have an allocated ip.

- Go to Route53 panel and create a new hosted zone. Then select and edit it, copy hosted zone id. 
- Modify next variables in .aws.env located at root project:
    -   DOMAIN # Registered domain in hosted zone (get it from Route53 panel)
    -   HOSTED_ZONE_ID # ID of hosted zone previously copied (get it from Route53 panel)
- Then execute `seed/docs/deployment/assets/aws-ec2/ec2.sh create-subdomain` which create a subdomain like <PROJECT_NAME>.<HOSTED_ZONE_DOMAIN>

### API-Worker Architecture

When deploying on AWS, it's important to consider divide Django & Celery in different instances. This allows for better resource allocation and scaling. The typical architecture involves:

1. **API Server (Django)**: This instance handles all incoming API requests. It runs the Django application and is responsible for processing user requests, interacting with the database, and returning responses.

2. **Worker Server (Celery)**: This instance runs the Celery worker processes. It is responsible for executing background tasks, such as sending emails, processing images, or any other long-running tasks that should not block the API server.

By separating these concerns, you can scale each component independently based on the load. For example, if you have a high volume of API requests, you can add more API servers without affecting the worker servers. Similarly, if you have a lot of background tasks, you can add more worker servers to handle the load. This architecture + load balancing ensures that no single instance becomes a bottleneck.

in order to configure this architecture on AWS, you need to set up separate EC2 instances for the API and worker components. Tag `app` for Django instances and `worker` for Celery instances. After that, you can use an Elastic Load Balancer (ELB) to distribute traffic between the API servers. Finally, setup .env file in AWS Secrets Manager for cloning the environment variables in each instance.

Then, copy `deployment/assets/load_balanced` files to the root and modify it with as project needs (check `<PROJECT>` and `<PROJECT_DOMAIN>` annotations). This will install the necessary dependencies and configure the services to run on the correct ports. Also updating changes with CodePipeline can be handled and deployed to the appropriate instances based on their tags.
