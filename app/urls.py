from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include
from graphene_django.views import GraphQLView
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    url(r'^api/', include('seed.app.api')),
    url(r'^api/', include('app.api')),
    url(r'^graphql$', csrf_exempt(GraphQLView.as_view(graphiql=True))),
    url(r'^admin/', admin.site.urls)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)