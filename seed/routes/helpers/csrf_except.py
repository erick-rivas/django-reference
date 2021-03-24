"""
__Seed builder__v0.2.0
  (Read_only) Builder helper
"""

from django.utils.deprecation import MiddlewareMixin


class CSRFDisableMiddleware(MiddlewareMixin):
    def process_request(self, request):
        setattr(request, '_dont_enforce_csrf_checks', True)