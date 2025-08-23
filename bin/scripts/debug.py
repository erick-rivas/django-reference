import os
import sys

if __name__ == "__main__":
    base_dir = os.path.dirname(os.path.realpath(__file__)) + '/../../'
    sys.path.insert(0, base_dir)

    import dotenv
    from app.settings import get_dotenv_path
    dotenv.read_dotenv(os.path.join(base_dir, get_dotenv_path()))
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "app.settings")

    import django
    django.setup()

    import debug_