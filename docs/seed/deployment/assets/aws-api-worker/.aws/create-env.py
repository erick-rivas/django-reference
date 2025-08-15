import boto3
import sys

def create_env_file(env_file_path, secret_name='secret'):
    secrets_manager = boto3.client('secretsmanager', region_name='us-east-1')
    with open(env_file_path, 'w') as env_file:
        response = secrets_manager.get_secret_value(SecretId=secret_name)
        secret = response['SecretString']
        env_file.write(secret)

if __name__ == '__main__':
    path = sys.argv[1]
    secret_name = sys.argv[2]
    create_env_file(path, secret_name)