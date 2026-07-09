"""
__Seed builder__
  (Read_only) Routes helper
"""

from django.http import HttpResponse
from django.views.decorators.cache import never_cache
from django.views.decorators.http import require_GET

@require_GET
@never_cache
def health(request):
    return HttpResponse(status=200)