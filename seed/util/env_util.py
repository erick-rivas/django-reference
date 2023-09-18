"""
__Seed builder__
  (Read_only) Environment variables util
"""
import os

def get_environ_bool(key):
    return True if key in os.environ and os.environ[key].lower() == "true" else False

def get_env_bool(key):
    return True if os.getenv(key) is not None and os.getenv(key).lower() == "true" else False

def get_dotenv_path():
    if get_environ_bool('USE_DOCKER'):
        return '.env.docker.prod' if get_environ_bool('IS_PROD') else '.env.docker.dev'
    return '.env.prod' if get_environ_bool('IS_PROD') else '.env.dev'