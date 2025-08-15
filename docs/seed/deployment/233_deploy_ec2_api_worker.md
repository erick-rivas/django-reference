### AWS EC2 API-Worker Architecture

When deploying on AWS, it's important to consider divide Django & Celery in different instances. This allows for better resource allocation and scaling. The typical architecture involves:

1. **API Server (Django)**: This instance handles all incoming API requests. It runs the Django application and is responsible for processing user requests, interacting with the database, and returning responses.

2. **Worker Server (Celery)**: This instance runs the Celery worker processes. It is responsible for executing background tasks, such as sending emails, processing images, or any other long-running tasks that should not block the API server.

By separating these concerns, you can scale each component independently based on the load. For example, if you have a high volume of API requests, you can add more API servers without affecting the worker servers. Similarly, if you have a lot of background tasks, you can add more worker servers to handle the load. This architecture + load balancing ensures that no single instance becomes a bottleneck.

in order to configure this architecture on AWS, you need to set up separate EC2 instances for the API and worker components. Tag `app` for Django instances and `worker` for Celery instances. After that, you can use an Elastic Load Balancer (ELB) to distribute traffic between the API servers. Finally, setup .env file in AWS Secrets Manager for cloning the environment variables in each instance.

Then, copy `deployment/assets/aws-api-worker` files to the root and modify it with as project needs (check `<PROJECT>` and `<PROJECT_DOMAIN>` annotations). This will install the necessary dependencies and configure the services to run on the correct ports. Also updating changes with CodePipeline can be handled and deployed to the appropriate instances based on their tags.