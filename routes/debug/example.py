"""
__Seed builder__
  AUTO_GENERATED (Read only)
  Example Viewset
  To include in project modify app.urls
"""

from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

class DebugViewSet(ViewSet):

    @action(detail=False, methods=['get'])
    def test(self, request):
        return Response("Test")