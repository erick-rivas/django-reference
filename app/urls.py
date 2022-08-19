"""
__Seed builder__
  Custom urls
  Example: /debug/test
      router = DefaultRouter()
      # TestView as rest_framework.viewsets.ViewSet Class
      router.register(r'test', TestViewSet, basename='test')
      urlpatterns += [
          path('debug/', include(debug_router.urls))
      ]
"""

from django.conf.urls import url
from django.urls import include, path

# pylint: disable=W0401
from seed.app.urls import *

## Include custom urls after here ##