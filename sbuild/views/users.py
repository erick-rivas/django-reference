"""
__Seed builder__v1.0
  (Read_only) Modify via SeedManifest.yaml
"""

from views.helpers.viewsets import ViewSet

from models.user import User
from serializers.user import UserSerializer

class _UserViewSet(ViewSet):  #

    serializer_class = UserSerializer
    queryset = User.objects.all()
