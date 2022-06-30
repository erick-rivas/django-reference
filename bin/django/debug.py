import os
import sys
import dotenv
import django

if __name__ == "__main__":
    base_dir = os.path.dirname(os.path.realpath(__file__)) + '/../../'
    sys.path.append(base_dir)
    from app.settings import get_dotenv

    dotenv.read_dotenv(os.path.join(base_dir, get_dotenv()))
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "app.settings")
    django.setup()
    import debug_