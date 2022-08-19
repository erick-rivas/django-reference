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
def send_mail_async(subject, plain_text, from_email, to_email, **kwargs):
    send_mail(subject, plain_text, from_email, to_email, **kwargs)