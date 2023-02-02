"""
__Seed builder__
  Custom urls
  Example: /debug/example/:actions
      from routes.debug.example import DebugViewSet
      ...
      debug_router = DefaultRouter()
      debug_router.register(r'example', DebugViewSet, basename='example')
      urlpatterns = [
          path('debug/', include(debug_router.urls))
      ] + urlpatterns
"""

from django.conf.urls import url
from django.urls import include, path

# pylint: disable=W0401
from seed.app.urls import *

## Include custom urls after here ##