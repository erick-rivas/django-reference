"""
__Seed builder__
  AUTO_GENERATED (Read only)
  Modify via builder
"""

import os

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path, re_path
from django.views.decorators.cache import never_cache
from django.views.generic import TemplateView, RedirectView
from django.views.static import serve
from seed.routes.helpers.graphene_view import graphene_view
from seed.routes.helpers.robot_view import robots_txt

urlpatterns = \
    [
        re_path(r'^api/', include('seed.app.api')),
        re_path(r'^graphql$', graphene_view()),
        re_path(r'^admin/', admin.site.urls),
        re_path("robots.txt", robots_txt),
    ]

urlpatterns += (
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
)

if settings.DEBUG:
    urlpatterns += [re_path("drf_auth/", include("rest_framework.urls")), ]

if os.path.exists((os.path.join(settings.REACTJS_DIR, "index.html"))):
    urlpatterns += \
        static("/theme", document_root=os.path.join(settings.REACTJS_DIR, "theme")) \
        + static("/resources", document_root=os.path.join(settings.REACTJS_DIR, "resources")) \
        + [re_path(r'^.*', never_cache(TemplateView.as_view(template_name='index.html')))]