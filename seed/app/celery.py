"""
__Seed builder__
  AUTO_GENERATED (Read only)
  Modify via builder
"""

import os
import dotenv
from datetime import timedelta

import sentry_sdk
from django.conf import settings
from django.core.mail import send_mail
from seed.helpers.clean_files import clean_files
from seed.util.env_util import get_env_bool, get_dotenv_path
from sentry_sdk.integrations.celery import CeleryIntegration

from celery import Celery
from celery import shared_task
from celery import signals

# General Settings

dotenv.read_dotenv(os.path.join(os.path.dirname(__file__), "..", "..", get_dotenv_path()))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings')
app = Celery('app')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
app.conf.update(
    CELERYD_PREFETCH_MULTIPLIER=1,
    CELERY_ACKS_LATE=True,
    CONCURRENCY=2,
    ACKS_ON_FAILURE_OR_TIMEOUT=True,
)

# Sentry init

@signals.celeryd_init.connect
def init_sentry(**kwargs):
    sentry_sdk.init(
        dsn=os.getenv('SENTRY_DSN', ""),
        integrations=[CeleryIntegration(monitor_beat_tasks=True)],
        environment="production" if settings.IS_PROD else "development",
        release="v1.0",
    )

# Common beat tasks

app.conf.beat_schedule = {}
if get_env_bool('ENABLE_FILE_CLEANING'):
    app.conf.beat_schedule['file_cleaning'] = {
        'task': 'seed.app.celery.clean_files_async',
        'schedule': timedelta(hours=1)
    }

# Common shared tasks

@shared_task
def send_mail_async(**kwargs):
    if "from_email" not in kwargs:
        kwargs["from_email"] = os.getenv('SMTP_EMAIL')
    send_mail(**kwargs)

@shared_task
def clean_files_async(dir_path=None, min_file_age=72):
    clean_files(dir_path, min_file_age)