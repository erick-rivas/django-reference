#!/bin/bash
# Clone secret environment file from AWS Secrets Manager

cd /home/ubuntu/<PROJECT>/
. .venv/bin/activate
python3 /home/ubuntu/<PROJECT>/aws/create-env.py /home/ubuntu/<PROJECT>/.env.dev secret-env-file