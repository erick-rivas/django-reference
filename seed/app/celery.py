"""
__Seed builder__
  AUTO_GENERATED (Read only)
  Modify via builder
"""

import os

import sentry_sdk
from celery import Celery
from celery import shared_task
from celery import signals
from django.conf import settings
from django.core.mail import send_mail
from sentry_sdk.integrations.celery import CeleryIntegration

# Settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings')
app = Celery('app')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

# Sentry settings
@signals.celeryd_init.connect
def init_sentry(**kwargs):
    sentry_sdk.init(
        dsn=os.getenv('SENTRY_DSN'),
        integrations=[CeleryIntegration(monitor_beat_tasks=True)],
        environment="production" if settings.IS_PROD else "development",
        release="v1.0",
    )

# Common shared tasks

@shared_task
def send_mail_async(**kwargs):
    if "from_email" not in kwargs:
        kwargs["from_email"] = os.getenv('SMTP_EMAIL')
    send_mail(**kwargs)