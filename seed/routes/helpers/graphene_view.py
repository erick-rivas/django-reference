"""
__Seed builder__
  (Read_only) Routes helper
"""

from graphene_django.views import GraphQLView
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt

class AuthGraphQLView(GraphQLView):
    @classmethod
    def as_view(cls, *args, **kwargs):
        view = super(AuthGraphQLView, cls).as_view(*args, **kwargs)
        view = api_view(['POST', 'GET'])(view)
        return view

    @classmethod
    def can_display_graphiql(cls, request, data):
        raw = "raw" in request.GET or "raw" in data
        is_dev_user = bool(request.user and request.user.is_superuser)
        return not raw and cls.request_wants_html(request) and is_dev_user

def graphene_view():
    return csrf_exempt(AuthGraphQLView.as_view(graphiql=True))