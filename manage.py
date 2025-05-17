#!/usr/bin/env python
"""
__Seed builder__
  AUTO_GENERATED (Read only)
  Modify via builder
"""
import os
import sys

import dotenv

if __name__ == "__main__":
    from seed.util.env_util import get_dotenv_path

    dotenv.read_dotenv(os.path.join(os.path.dirname(__file__), get_dotenv_path()))
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "app.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError:
        try:
            import django

            print(django.VERSION)
        except ImportError:
            raise ImportError(
                "Couldn't import Django. Are you sure it's installed and "
                "available on your PYTHONPATH environment variable? Did you "
                "forget to activate a virtual environment?"
            )
        raise
    execute_from_command_line(sys.argv)