from views.helpers.viewsets import ReadOnlyViewSet
from models.user import User
from serializers.user import UserSerializer

class UserViewSet(ReadOnlyViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
