import os
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include
from graphene_django.views import GraphQLView
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView
from django.views.decorators.cache import never_cache


urlpatterns = [
    url(r'^api/', include('seed.app.api')),
    url(r'^api/', include('app.api')),
    url(r'^graphql$', csrf_exempt(GraphQLView.as_view(graphiql=True))),
    url(r'^admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) \
  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if os.path.exists((os.path.join(settings.BASE_DIR, "reactjs", "index.html"))):
    reactjs = never_cache(TemplateView.as_view(template_name='index.html'))
    urlpatterns += [url(r'^.*', reactjs)]