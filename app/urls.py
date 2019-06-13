"""
__Seed builder__v1.0
  Guidelines: 
    - Modify api includes via models.json
"""

from django.conf.urls import url
from django.contrib import admin
from django.urls import include
from rest_framework_swagger.views import get_swagger_view

docs = get_swagger_view(title='Django reference')

urlpatterns = [
    url(r'^api/', include('_seed.app.api')),
    url(r'^api/', include('app.api')),
    url(r'^admin/', admin.site.urls),
    url(r'^docs/', docs),
]