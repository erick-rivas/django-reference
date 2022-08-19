"""
__Seed builder__
  (Read_only) Model helper
"""

from django.db import models
from seed.models.model import Model


class File(Model):

    url = models.URLField(
        max_length=1024, help_text="File reference link (eg. http://localhost:8000/image.png)")
    size = models.IntegerField(help_text="File size in bytes", default=0, null=True, blank=True)
    name = models.CharField(
        max_length=1024, help_text="Common File Name (eg. Image.png)", default="",
        null=True, blank=True)

    class Meta:
        db_table = 'file'
        app_label = 'models'