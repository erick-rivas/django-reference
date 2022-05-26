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
def send_email_async(**kwargs):
    send_mail(**kwargs)

# Custom tasks