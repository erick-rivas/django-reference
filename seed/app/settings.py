"""
__Seed builder__
  AUTO_GENERATED (Read only)
  Modify via builder
"""

import os
import dotenv
import sentry_sdk
from django.core.management.commands.runserver import Command as runserver
from sentry_sdk.integrations.django import DjangoIntegration
from urllib.parse import urlparse
from seed.util.env_util import get_environ_bool, get_env_bool, get_dotenv_path

BASE_DIR = os.path.dirname(
               os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..",))
dotenv.read_dotenv(os.path.join(BASE_DIR, get_dotenv_path()))
runserver.default_port = '8008'

IS_PROD = get_environ_bool('IS_PROD')
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

STATIC_ROOT = os.path.join(BASE_DIR, "static")
STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, "models", "fixtures", "media"), ]
MEDIA_ROOT = os.path.join(BASE_DIR, "media")
MEDIA_URL = '/media/'

USE_AWS_S3 = get_env_bool('USE_AWS_S3')
if USE_AWS_S3:
    AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
    AWS_STORAGE_BUCKET_NAME = os.getenv('AWS_STORAGE_BUCKET_NAME')
    AWS_S3_REGION_NAME = os.getenv('AWS_S3_REGION_NAME')
    AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
    DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
    MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/media/'

# Libs & definition

INSTALLED_APPS = [

    # System constance
    'constance',

    # Models
    'models',

    # Libs
    'daphne',
    'rest_framework',
    'rest_framework.authtoken',
    'django_filters',
    'import_export',
    'djangoql',
    'corsheaders',
    'graphene_django',
    'channels',
    'dj_rest_auth',
    'storages',
    'django_celery_beat',

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

REQUIRE_SSLMODE = get_env_bool("DB_SSL")
if REQUIRE_SSLMODE:
    DATABASES['default']['OPTIONS'] = {'sslmode': 'require'}

# Constance settings

CONSTANCE_CONFIG = {
    'LATEST_VERSION': ("1.0", 'Latest version of the system', str),
    'UNDER_MAINTENANCE': (False, 'Flag to define if it is under maintenance or not', bool)
}

CONSTANCE_BACKEND = 'constance.backends.database.DatabaseBackend'

# Security settings

REST_AUTH = {
    'TOKEN_SERIALIZER': 'seed.serializers.helpers.token.TokenSerializer',
    'USER_DETAILS_SERIALIZER': 'seed.serializers.user.UserSerializer'
}
CORS_ORIGIN_WHITELIST = [os.getenv('CLIENT_URL'), ]
ALLOWED_HOSTS = ['localhost', '127.0.0.1', '[::1]', urlparse(os.getenv('SERVER_URL')).hostname]
if get_env_bool('FORCE_SSL'):
    SECURE_SSL_REDIRECT = True
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator', },
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator', },
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator', },
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator', },
]

# Sentry settings

sentry_sdk.init(
    dsn=os.getenv('SENTRY_DSN', ""),
    integrations=[DjangoIntegration()],
    environment="production" if IS_PROD else "development",
    send_default_pii=True,
    traces_sample_rate=float(os.getenv('SENTRY_SAMPLE_RATE', "0.05")),
    profiles_sample_rate=1.0
)

# Templates settings

TEMPLATES_DIRS = [os.path.join(BASE_DIR, 'templates'), os.path.join(BASE_DIR, 'seed', 'templates')]
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

# DRF Settings

REST_FRAMEWORK = {}
REST_FRAMEWORK['DEFAULT_RENDERER_CLASSES'] = [
    'rest_framework.renderers.JSONRenderer',
    'seed.routes.helpers.rest_render.BrowsableAPIRenderer',
]

REST_FRAMEWORK['DEFAULT_AUTHENTICATION_CLASSES'] = [
    'rest_framework.authentication.TokenAuthentication',
]
REST_FRAMEWORK['DEFAULT_PERMISSION_CLASSES'] = ['rest_framework.permissions.IsAuthenticated', ]

GRAPHENE = {'SCHEMA': 'seed.app.graphene.schema'}

# Celery

CELERY_BROKER_URL = 'redis://' + os.getenv('REDIS_HOST') + ':' + os.getenv('REDIS_PORT')
CELERY_SETTINGS = {
    'broker_url': CELERY_BROKER_URL,
    'result_backend': CELERY_BROKER_URL,
    'accept_content': ['application/json'],
    'timezone': 'America/Mexico_City',
    'worker_prefetch_multiplier': 1
}

# Channels

CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            'hosts': [(os.getenv('REDIS_HOST'), os.getenv('REDIS_PORT'))],
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

LANGUAGE_CODE = 'es-mx'
TIME_ZONE = 'America/Mexico_City'
USE_I18N = True
USE_L10N = True
USE_TZ = True