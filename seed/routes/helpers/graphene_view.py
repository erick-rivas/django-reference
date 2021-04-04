"""
__Seed builder__v0.2.0
  (Read_only) Builder helper
"""

from graphene_django.views import GraphQLView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import authentication_classes, permission_classes, api_view
from django.views.decorators.csrf import csrf_exempt
from app.settings import get_env


class AuthGraphQLView(GraphQLView):
    @classmethod
    def as_view(cls, *args, **kwargs):
        view = super(AuthGraphQLView, cls).as_view(*args, **kwargs)
        view = permission_classes((IsAuthenticated,))(view)
        view = authentication_classes((TokenAuthentication,))(view)
        view = api_view(['POST'])(view)
        return view


def graphene_view():
    if get_env('ENABLE_AUTH'):
        return csrf_exempt(AuthGraphQLView.as_view(graphiql=True))
    return csrf_exempt(GraphQLView.as_view(graphiql=True))