from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include
from rest_framework_swagger.views import get_swagger_view

docs = get_swagger_view(title='Django reference')

urlpatterns = [
    url(r'^api/', include('seed.app.api')),
    url(r'^api/', include('app.api')),
    url(r'^admin/', admin.site.urls),
    url(r'^docs/', docs),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)