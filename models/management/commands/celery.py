"""
__Seed builder__
  AUTO_GENERATED command (Read only)
"""

import shlex
import subprocess # nosec B404
import sys

from django.core.management.base import BaseCommand
from django.utils import autoreload

def restart_celery():
    celery_worker_cmd = "celery -A seed.app worker -l INFO -B"
    cmd = f'pkill -f "{celery_worker_cmd}"'
    if sys.platform == "win32":
        cmd = "taskkill /f /t /im celery.exe"

    subprocess.call(shlex.split(cmd)) # nosec B603
    subprocess.call(shlex.split(f"{celery_worker_cmd} --loglevel=info")) # nosec B603

class Command(BaseCommand):
    def handle(self, *args, **options):
        print("Starting celery worker with autoreload...")
        autoreload.run_with_reloader(restart_celery)