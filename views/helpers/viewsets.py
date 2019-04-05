from rest_framework import mixins
from rest_framework import viewsets
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


class BaseViewSet(viewsets.GenericViewSet,
                  mixins.ListModelMixin,
                  mixins.RetrieveModelMixin):
    """ Enable security
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    """
    lookup_field = 'uuid'
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter,)
    filterset_fields = '__all__'
    ordering_fields = '__all__'

class CreateViewSet(BaseViewSet,
                    mixins.CreateModelMixin,
                    mixins.UpdateModelMixin):
    pass

class FullViewSet(CreateViewSet,
                  mixins.DestroyModelMixin):
    pass
