"""
__Seed builder__
  AUTO_GENERATED (Read only)
  Modify via builder
"""

import os
from celery import Celery
from celery import shared_task
from datetime import datetime, timedelta
from django.core.mail import send_mail

# Settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings')
app = Celery('app')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

# Celery beat config tasks

app.conf.beat_schedule = {
    'execute_file_cleaning': {
        'task': 'seed.app.celery.clean_files',
        'schedule': timedelta(hours=1)
    }
}

app.conf.update(
    CELERYD_PREFETCH_MULTIPLIER=1,
    CELERY_ACKS_LATE=True,
    CONCURRENCY=2,
    ACKS_ON_FAILURE_OR_TIMEOUT=True,
)


# Common shared tasks

@shared_task
def send_mail_async(subject, plain_text, from_email, to_email, **kwargs):
    send_mail(subject, plain_text, from_email, to_email, **kwargs)


@shared_task
def clean_files():

    from seed.models.file import File
    from seed.app.settings import MEDIA_ROOT

    try:
        file_names = os.listdir(MEDIA_ROOT)
        for file_name in file_names:

            if not File.objects.filter(name=file_name).exists():
                timestamp = os.path.getctime(MEDIA_ROOT)
                created_at = datetime.fromtimestamp(timestamp)

                difference = datetime.now() - created_at
                seconds = difference.total_seconds()
                minutes = seconds / 60
                hours = minutes / 60

                if hours > 24:
                    os.remove(os.path.join(MEDIA_ROOT, file_name))

    except Exception: 
        pass
