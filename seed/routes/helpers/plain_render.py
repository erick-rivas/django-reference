"""
__Seed builder__
  (Read_only) Routes helper
"""

from rest_framework.renderers import BaseRenderer
from django.utils.encoding import smart_str

class PlainTextRenderer(BaseRenderer):
    
    media_type = 'text/plain'
    format = 'txt'

    def render(self, data, accepted_media_type=None, renderer_context=None):
        return smart_str(data, encoding=self.charset)