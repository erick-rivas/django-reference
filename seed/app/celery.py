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
app.config_from_object(settings.CELERY_SETTINGS)
app.autodiscover_tasks()

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

# Common shared tasks

@shared_task
def send_mail_async(subject, message, recipient_list, from_email=None, **kwargs):
    if from_email is None:
        from_email = os.getenv('SMTP_EMAIL')
    send_mail(
        subject,
        message,
        from_email,
        recipient_list,
        **kwargs
    )