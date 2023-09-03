"""
__Seed builder__
  Custom urls
  Example: /debug/:viewset_actions
      from routes.debug.example import ExampleViewSet
      ...
      debug_router = DefaultRouter()
      debug_router.register(r'', ExampleViewSet, basename='')

      # Special condition to prevent leaks in production,
      # it can be omitted for non-debug viewsets
      if settings.DEBUG:
          urlpatterns = [
              re_path('^debug/', include(debug_router.urls))
          ] + urlpatterns
"""

from rest_framework.routers import DefaultRouter

# pylint: disable=W0401
from seed.app.urls import *

## Include custom urls after here ##