"""
__Seed builder__v1.0
"""

from views.helpers.viewsets import FullViewSet

from models.user import User
from serializers.user import UserSerializer

class _UserViewSet(FullViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
