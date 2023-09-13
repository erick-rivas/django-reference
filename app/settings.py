"""
__Seed builder__
  Custom settings
  Examples:
      INSTALLED_APPS += ["new_apps"]
      ALLOWED_HOSTS = ["*",]
"""

# pylint: disable=W0401
from seed.app.settings import *
import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

## Include custom settings after here ##
sentry_sdk.init(
    dsn="",
    integrations=[DjangoIntegration()],
    traces_sample_rate=1.0
)