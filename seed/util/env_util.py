"""
__Seed builder__
  (Read_only) Environment variables util
"""
import os

def get_environ(key):
    return True if key in os.environ and os.environ[key].lower() == "true" else False

def get_env(key):
    return True if os.getenv(key) is not None and os.getenv(key).lower() == "true" else False

def get_dotenv():
    if get_environ('USE_DOCKER'):
        return '.env.docker.prod' if get_environ('IS_PROD') else '.env.docker.dev'
    return '.env.prod' if get_environ('IS_PROD') else '.env.dev'