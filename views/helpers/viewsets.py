from rest_framework import mixins
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

class BaseViewSet(viewsets.GenericViewSet,
                  mixins.ListModelMixin,
                  mixins.RetrieveModelMixin):
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
