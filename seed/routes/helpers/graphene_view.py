"""
__Seed builder__
  (Read_only) Routes helper
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
        view = api_view(['POST', 'GET'])(view)
        return view

def graphene_view():
    return csrf_exempt(AuthGraphQLView.as_view(graphiql=True))