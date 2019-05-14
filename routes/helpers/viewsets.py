from rest_framework import mixins
from rest_framework import viewsets
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


class BaseViewSet(viewsets.GenericViewSet):
    """ Enable security
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    """

class ReadOnlyViewSet(
    BaseViewSet,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin):
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter,)
    filterset_fields = '__all__'
    ordering_fields = '__all__'

class WriteOnlyViewSet(
    BaseViewSet,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin):
    pass

class ReadWriteViewSet(
    ReadOnlyViewSet,
    WriteOnlyViewSet):
    pass

class WriteDeleteViewSet(
    WriteOnlyViewSet,
    mixins.DestroyModelMixin):
    pass

class FullViewSet(
    ReadWriteViewSet,
    mixins.DestroyModelMixin):
    pass
