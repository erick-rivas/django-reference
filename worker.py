#!/usr/bin/env python
import os
import sys

import django

import dotenv

if __name__ == "__main__":
    base_dir = os.path.dirname(os.path.realpath(__file__)) + '/../../'
    sys.path.append(base_dir)
    from app.settings import get_dotenv_path

    dotenv.read_dotenv(os.path.join(base_dir, get_dotenv_path()))
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "app.settings")
    django.setup()

    from django.utils import autoreload

    def run_celery():
        from app.celery import app as celery_app
        args = "-A seed.app worker -l INFO -B"
        celery_app.worker_main(args.split(" "))

    print("Starting celery worker with autoreload...")
    autoreload.run_with_reloader(run_celery)