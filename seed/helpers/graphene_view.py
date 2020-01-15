"""
__Seed builder__v0.1.8
  (Read_only) Builder helper
"""

from graphene_django.views import GraphQLView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.views.decorators.csrf import csrf_exempt
from app.settings import get_env

from graphene_django.views import GraphQLView
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import authentication_classes, permission_classes, api_view

class AuthGraphQLView(GraphQLView):
    @classmethod
    def as_view(self, *args, **kwargs):
        view = super(AuthGraphQLView, self).as_view(*args, **kwargs)
        view = permission_classes((IsAuthenticated,))(view)
        view = authentication_classes((TokenAuthentication,))(view)
        view = api_view(['POST'])(view)
        return view

def graphene_view():
    if get_env('ENABLE_AUTH'):
        return csrf_exempt(AuthGraphQLView.as_view(graphiql=True))
    return csrf_exempt(GraphQLView.as_view(graphiql=True))