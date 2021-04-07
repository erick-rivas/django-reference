import os

from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.views.decorators.cache import never_cache
from django.views.generic import TemplateView, RedirectView
from seed.routes.helpers.graphene_view import graphene_view

urlpatterns = \
    [
        url(r'^api/', include('seed.app.api')),
        url(r'^api/', include('app.api')),
        url(r'^graphql$', graphene_view()),
        url(r'^admin/', admin.site.urls),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) \
    + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG and os.path.exists((os.path.join(settings.DOCS_DIR, "index.html"))):
    urlpatterns += \
        [url(r'^docs$', RedirectView.as_view(url='./docs/010_general.html'))] \
        + static("/docs", document_root=settings.DOCS_DIR)

if os.path.exists((os.path.join(settings.REACTJS_DIR, "index.html"))):
    urlpatterns += \
        [url(r'^.*', never_cache(TemplateView.as_view(template_name='index.html')))] \
        + static(settings.STATIC_URL, document_root=settings.REACTJS_DIR)