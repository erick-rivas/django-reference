"""
__Seed builder__
  AUTO_GENERATED (Read only)
  Modify via builder
"""

import os

from celery import Celery

# Settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings')
app = Celery('app')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()