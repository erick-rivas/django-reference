"""
__Seed builder__
  AUTO_GENERATED (Read only)
  Modify via builder
"""

import re
from urllib.parse import urlsplit

from django.core.exceptions import ImproperlyConfigured
from django.urls import re_path
from django.views.static import serve

def custom_static(prefix, view=serve, **kwargs):
    # Overridden  from django.conf.urls.static.static
    if not prefix:
        raise ImproperlyConfigured("Empty static prefix not permitted")
    elif urlsplit(prefix).netloc:
        return []
    return [re_path(r'^%s(?P<path>.*)$' % re.escape(prefix.lstrip('/')), view, kwargs=kwargs), ]