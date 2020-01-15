import os
import dotenv
from urllib.parse import urlparse

def get_environ(key):
    return True if key in os.environ and os.environ[key].lower() == "true" else False

def get_env(key):
    return True if os.getenv(key) is not None and os.getenv(key).lower() == "true" else False

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
IS_PROD = get_environ('IS_PROD')
dotenv.read_dotenv(os.path.join(os.path.dirname(os.path.dirname(__file__)),
    '.env.prod' if IS_PROD else '.env.dev'))

USE_AWS_EB = get_env('USE_AWS_EB')
USE_AWS_S3 = get_env('USE_AWS_S3')
DEBUG = not IS_PROD
SECRET_KEY = 'fup+swltefA9efredrufihUSTO!wam?c'
SITE_ID = 1

# General settings

ROOT_URLCONF = 'app.urls'
WSGI_APPLICATION = 'app.wsgi.application'
AUTH_USER_MODEL = 'models.User'
FIXTURE_DIRS = (os.path.join(BASE_DIR, "fixtures"),)

# Files definitions

STATIC_ROOT = os.path.join(BASE_DIR, "static")
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "reactjs", "static"),
    os.path.join(BASE_DIR, "fixtures", "media")
]
MEDIA_ROOT = os.path.join(BASE_DIR, "media")
MEDIA_URL = '/media/'

# Libs & definition

INSTALLED_APPS = [

    # Models
    'models',

    # Libs
    'rest_framework',
    'dynamic_rest',
    'rest_framework.authtoken',
    'rest_auth',
    'django_filters',
    'import_export',
    'djangoql',
    'corsheaders',
    'graphene_django',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'seed.helpers.csrf_except.CSRFDisableMiddleware',
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
} if not USE_AWS_EB else {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ['RDS_DB_NAME'],
        'USER': os.environ['RDS_USERNAME'],
        'PASSWORD': os.environ['RDS_PASSWORD'],
        'HOST': os.environ['RDS_HOSTNAME'],
        'PORT': os.environ['RDS_PORT']
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
CORS_ORIGIN_WHITELIST = [os.getenv('APP_URL')]
ALLOWED_HOSTS = [urlparse(os.getenv('HOST_URL')).hostname]

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator', },
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator', },
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator', },
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator', },
]

# Templates settings

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'reactjs')],
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
        'dynamic_rest.renderers.DynamicBrowsableAPIRenderer',
    ],
}

DYNAMIC_REST = {'ENABLE_LINKS': False}

GRAPHENE = {
    'SCHEMA': 'app.graphene.schema'
}

# EMAIL

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST_USER = os.getenv('SMTP_EMAIL')
EMAIL_HOST_PASSWORD = os.getenv('SMTP_PASSWORD')
EMAIL_HOST = os.getenv('SMTP_HOST')
EMAIL_PORT = os.getenv('SMTP_PORT')
EMAIL_USE_SSL = True

# Internationalization

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True