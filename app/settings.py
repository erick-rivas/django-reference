"""
__Seed builder__
  Custom settings
  Examples:
      INSTALLED_APPS += ["new_apps"]
      ALLOWED_HOSTS = ["*",]
      CONSTANCE_CONFIG += [(123, 'Internal setting description', int)]
"""

# pylint: disable=W0401
from seed.app.settings import *

## Include custom settings after here ##