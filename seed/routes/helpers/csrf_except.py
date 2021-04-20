"""
__Seed builder__
  (Read_only) Routes helper
"""

from django.utils.deprecation import MiddlewareMixin


class CSRFDisableMiddleware(MiddlewareMixin):
    def process_request(self, request):
        setattr(request, '_dont_enforce_csrf_checks', True)