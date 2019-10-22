"""
__Seed builder__v0.1.8
  AUTO_GENERATED (Read only)
  Modify via builder
"""

from seed.helpers.viewsets import ViewSet

from app.models import User
from app.serializers import UserSerializer

class _UserViewSet(ViewSet):  #

    serializer_class = UserSerializer
    queryset = User.objects.all()
