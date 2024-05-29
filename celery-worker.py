# pylint: disable=C0103
import os
import shlex
import subprocess  # nosec B404
import sys

import dotenv

if __name__ == "__main__":
    from seed.util.env_util import get_dotenv_path

    dotenv.read_dotenv(os.path.join(os.path.dirname(__file__), get_dotenv_path()))
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "app.settings")
    import django

    django.setup()

    from django.utils import autoreload

    def restart_celery():
        celery_worker_cmd = "celery -A seed.app worker -l INFO -B"
        cmd = f'pkill -f "{celery_worker_cmd}"'
        if sys.platform == "win32":
            cmd = "taskkill /f /t /im celery.exe"

        subprocess.call(shlex.split(cmd))  # nosec B603
        subprocess.call(shlex.split(f"{celery_worker_cmd} --loglevel=info"))  # nosec B603

    print("Starting celery worker with autoreload...")
    autoreload.run_with_reloader(restart_celery)