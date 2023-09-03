"""
__Seed builder__
  AUTO_GENERATED (Read only)
  Modify via builder
"""

import os

from celery import Celery
from celery import shared_task
from django.core.mail import send_mail

# Settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings')
app = Celery('app')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

# Common shared tasks

@shared_task
def send_mail_async(**kwargs):
    if "from_email" not in kwargs:
        kwargs["from_email"] = os.getenv('SMTP_EMAIL')
    send_mail(**kwargs)