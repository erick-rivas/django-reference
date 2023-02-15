## AWS Code Deploy

### Install AWS CLI

Execute the followings commands:

```bash
sudo apt install unzip
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
unzip awscliv2.zip
sudo ./aws/install
```

Add secret AWS keys in bin/aws/files/.aws.env (you can create an IAM user or get them from Account >> Security Credentials)
- AWS_ACCESS_KEY_ID
- AWS_SECRET_ACCESS_KEY

Note: if you need to specify a region, modify also REGION and BUCKET_NAME (get BUCKET_NAME and region identifier from [https://docs.aws.amazon.com/codedeploy/latest/userguide/resource-kit.html#resource-kit-bucket-names](https://docs.aws.amazon.com/codedeploy/latest/userguide/resource-kit.html#resource-kit-bucket-names))

Then execute `bin/aws/configure.sh` to set cli keys

### Configure CodeDeploy

Modify next variables in bin/aws/files/.aws.env
- ARN_CONNECTION # CodeStar GitHub connection
- REPOSITORY # Repository id (for example, <user>/<repository_name>)
- PROJECT_NAME # Custom name (like reference-api)
- INSTANCE_ID # Server instance id
- INSTANCE_NAME # Server instance name
- ARN_ROLE_CD # ARN of CodeDeploy IAM role 
- ARN_ROLE_PL # ARN of CodePipeline IAM role
- ARTIFACT_BUCKET # S3 bucket for pipeline

Follow next steps:
- Create and associate roles: `bin/aws/codedeploy.sh --config`
- Install AWS Agent: `bin/aws/codedeploy.sh --install` (to check status use `sudo service codedeploy-agent status`)
- Create CodeDeploy application: `bin/aws/codedeploy.sh --create-app`
- Create a Deployment Group: `bin/aws/codedeploy.sh --create-dg`
- Create new pipeline: `bin/aws/codedeploy.sh --create-pl`