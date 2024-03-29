## AWS EC2

### Setup EC2 instance

Go to EC2 panel and click on Launch instance. 
Then follow the default steps to create a instance. At this point extract instance id and name from EC2 panel >> Instance submenu.

After creating the instance connect via ssh `ssh -i <GENERATE.pem> ubuntu@<INSTANCE_IP>`  and execute the steps in [ubuntu docs](../210_deploy_ubuntu.md)

### Install AWS CLI

Execute the followings commands:

```bash
sudo apt install unzip
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
unzip awscliv2.zip
sudo ./aws/install
```

Copy seed/docs/extras/assets/aws-ec2/.env.example to root project and rename to **.aws.env**.
Request to admin secret AWS keys (you can also create an IAM user or get them from Account >> Security Credentials) and modify next variables in .aws.env located at root project:
-   AWS_ACCESS_KEY_ID
-   AWS_SECRET_ACCESS_KEY

Note: if you need to specify a region, modify also REGION and BUCKET_NAME (get BUCKET_NAME and region identifier from [https://docs.aws.amazon.com/codedeploy/latest/userguide/resource-kit.html#resource-kit-bucket-names](https://docs.aws.amazon.com/codedeploy/latest/userguide/resource-kit.html#resource-kit-bucket-names))

Then execute `seed/docs/extras/assets/aws-ec2/configure.sh` to set cli keys

### Configure

Request to admin instance id and name. Then Modify next variables in .aws.env located at root project:
-   INSTANCE_ID # Server instance id
-   INSTANCE_NAME # Server instance name
-   PROJECT_NAME # Custom name (custom name like reference-api)

### Available CLI commands

Available options are:

-   `seed/docs/extras/assets/aws-ec2/ec2.sh start` # Start server
-   `seed/docs/extras/assets/aws-ec2/ec2.sh stop` # Stop server, you can't access once it's stopped
-   `seed/docs/extras/assets/aws-ec2/ec2.sh restart` # Restart server
-   `seed/docs/extras/assets/aws-ec2/ec2.sh allocate-ip` # Allocate an elastic ip and associate it to server

### See also

-   [EC2 Codedeploy](231_deploy_ec2_codedeploy.md)
-   [EC2 Extras](232_deploy_ec2_extras.md)