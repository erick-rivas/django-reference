### Initialization

/home/ubuntu/<PROJECT>/.aws/single-install.sh
/home/ubuntu/<PROJECT>/.aws/create-env.sh

pip3 install boto3

# Get instance metadata
INSTANCE_ID=$(ec2metadata --instance-id)

# Get instance type
INSTANCE_TYPE=$(python3 - <<END
import boto3

ec2 = boto3.client('ec2', region_name='us-east-1')

response = ec2.describe_instances(InstanceIds=['$INSTANCE_ID'])
tags = response['Reservations'][0]['Instances'][0].get('Tags', [])

for tag in tags:
    if tag['Key'] == 'Name':
        print(tag['Value'])
        break
else:
    print('unknown')
END
)

### Deployment

/home/ubuntu/<PROJECT>/requirements.libs

if [ "$INSTANCE_TYPE" == "app" ]; then
  /home/ubuntu/<PROJECT>/.aws/setup-nginx.sh
  /home/ubuntu/<PROJECT>/.aws/setup-daphne.sh
  /home/ubuntu/<PROJECT>/.aws/deploy-api.sh
elif [ "$INSTANCE_TYPE" == "worker" ]; then
  /home/ubuntu/<PROJECT>/.aws/setup-celery.sh
  /home/ubuntu/<PROJECT>/.aws/deploy-celery.sh
fi