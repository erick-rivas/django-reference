## AWS Code Deploy

### Before start

Before start implementing, check [ubuntu setup](220_ubuntu.md) and also [ec2 setup](222_ec2.md)

### Configure CodeDeploy

Modify next variables in .aws.env located at root project:
-   ARN_CONNECTION # CodeStar GitHub connection (get it from CodeDeploy >> Connections panel) 
-   REPOSITORY # Repository id (user/repository_name), example: `erick-rivas/django-reference`
-   ARTIFACT_BUCKET # S3 bucket name for pipeline (get it from S3 panel)

Follow next steps:
-   Create and associate roles: `seed/docs/assets/aws-code-deploy/codedeploy.sh config`
-   Install AWS Agent: `seed/docs/assets/aws-code-deploy/codedeploy.sh install-<version>` (available versions are 20 and 22). Note, to check status use `sudo service codedeploy-agent status`
-   Create CodeDeploy application: `seed/docs/assets/aws-code-deploy/codedeploy.sh create-app`
-   Create a Deployment Group: `seed/docs/assets/aws-code-deploy/codedeploy.sh create-dg`
-   Create new pipeline: `seed/docs/assets/aws-code-deploy/codedeploy.sh create-pl`

### Configure file

-   Modify appspec.yml in root project as you need.
	-	version: current version of the spec file
	-	os: environment operating system
	-	files: location of the project (this will be join with hooks location param)
	-	permissions: specification of file access
	-	hooks: execution of scripts before each lifecycle stage of codedeploy, these are
		-	BeforeInstall
		-	AfterInstall
		-	ApplicationStart
		-	ApplicationStop
		Note: inside these stages you can specify the location of script, timeout and user who run it.
		
	For more specification, you can visit [https://docs.aws.amazon.com/codedeploy/latest/userguide/reference-appspec-file.html](https://docs.aws.amazon.com/codedeploy/latest/userguide/reference-appspec-file.html)