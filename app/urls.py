from django.conf.urls import url
from django.contrib import admin

from django.urls import include

from rest_framework_swagger.views import get_swagger_view

docs = get_swagger_view(title='Django reference')

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^docs/', docs),
    url(r'^v1/', include('app.api')),
]