"""
__Seed builder__
  AUTO_GENERATED (Read only)
  Modify via builder
"""

import os
from urllib.parse import urlparse

import dotenv

def get_environ(key):
    return True if key in os.environ and os.environ[key].lower() == "true" else False

def get_env(key):
    return True if os.getenv(key) is not None and os.getenv(key).lower() == "true" else False

def get_dotenv():
    if get_environ('USE_DOCKER'):
        return '.env.docker.prod' if get_environ('IS_PROD') else '.env.docker.dev'
    return '.env.prod' if get_environ('IS_PROD') else '.env.dev'

BASE_DIR = os.path.dirname(
               os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..",))
dotenv.read_dotenv(os.path.join(BASE_DIR, get_dotenv()))

IS_PROD = get_environ('IS_PROD')
DEBUG = not IS_PROD
SECRET_KEY = os.getenv('SECRET_KEY')

# General settings

ROOT_URLCONF = 'app.urls'
WSGI_APPLICATION = 'seed.app.wsgi.application'
ASGI_APPLICATION = 'seed.app.asgi.application'
AUTH_USER_MODEL = 'models.User'
DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'
SITE_ID = 1

# Files definitions

USE_AWS_S3 = get_env('USE_AWS_S3')
STATIC_ROOT = os.path.join(BASE_DIR, "static")
STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, "models", "fixtures", "media"), ]
MEDIA_ROOT = os.path.join(BASE_DIR, "media")
MEDIA_URL = '/media/'

# Libs & definition

INSTALLED_APPS = [

    # Models
    'models',

    # Libs
    'rest_framework',
    'rest_framework.authtoken',
    'rest_auth',
    'django_filters',
    'import_export',
    'djangoql',
    'corsheaders',
    'graphene_django',
    'channels',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'seed.routes.helpers.csrf_except.CSRFDisableMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Database settings

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('DB_NAME'),
        'USER': os.getenv('DB_USER'),
        'PASSWORD': os.getenv('DB_PASSWORD'),
        'HOST': os.getenv('DB_HOST'),
        'PORT': os.getenv('DB_PORT')
    }
}

# S3 Settings

if USE_AWS_S3:
    DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
    AWS_ACCESS_KEY_ID = os.getenv('AWS_S3_KEY')
    AWS_SECRET_ACCESS_KEY = os.getenv('AWS_S3_SECRET')
    AWS_STORAGE_BUCKET_NAME = os.getenv('AWS_S3_BUCKET_NAME')
    AWS_DEFAULT_ACL = "public-read"
    AWS_BUCKET_ACL = "public-read"
    AWS_AUTO_CREATE_BUCKET = True

# Security settings

REST_AUTH_SERIALIZERS = {'TOKEN_SERIALIZER': 'seed.serializers.helpers.token.TokenSerializer'}
CORS_ORIGIN_WHITELIST = [os.getenv('CLIENT_URL')]
ALLOWED_HOSTS = ['localhost', '127.0.0.1', '[::1]', urlparse(os.getenv('SERVER_URL')).hostname]
if get_env('USE_HTTPS'):
    SECURE_SSL_REDIRECT = True
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator', },
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator', },
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator', },
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator', },
]

# Templates settings

TEMPLATES_DIRS = [os.path.join(BASE_DIR, 'templates'), os.path.join(BASE_DIR, 'seed', 'templates')]
DOCS_DIR = os.path.join(BASE_DIR, ".data", "docs")
REACTJS_DIR = os.path.join(BASE_DIR, "reactjs")
if os.path.exists((os.path.join(REACTJS_DIR, "index.html"))):
    STATICFILES_DIRS += [os.path.join(REACTJS_DIR, "static"), ]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': TEMPLATES_DIRS + [REACTJS_DIR, ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer'
    ],
} if DEBUG else {
    'DEFAULT_RENDERER_CLASSES': [
        'seed.routes.helpers.rest_render.ProductionBrowsableAPIRenderer'
    ],
}
REST_FRAMEWORK['DEFAULT_AUTHENTICATION_CLASSES'] = \
    ['rest_framework.authentication.TokenAuthentication',]

GRAPHENE = {
    'SCHEMA': 'seed.app.graphene.schema'
}

# Celery

CELERY_BROKER_URL = 'redis://' + os.getenv("REDIS_HOST") + ':' + os.getenv("REDIS_PORT")
CELERY_RESULT_BACKEND = CELERY_BROKER_URL
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = 'America/Mexico_City'

# Channels

CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels_redis.core.RedisChannelLayer",
        "CONFIG": {
            "hosts": [(os.getenv("REDIS_HOST"), os.getenv("REDIS_PORT"))],
        }
    }
}

# Email

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST_USER = os.getenv('SMTP_EMAIL')
EMAIL_HOST_PASSWORD = os.getenv('SMTP_PASSWORD')
EMAIL_HOST = os.getenv('SMTP_HOST')
EMAIL_PORT = os.getenv('SMTP_PORT')
EMAIL_USE_SSL = False
EMAIL_USE_TLS = True

# Internationalization

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'America/Mexico_City'
USE_I18N = True
USE_L10N = True
USE_TZ = True