from serializers.user import UserSerializer
from views.helpers.viewsets import ReadOnlyViewSet
from models.user import User

class UserViewSet(ReadOnlyViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
