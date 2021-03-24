"""
__Seed builder__v0.2.0
  (Read_only) Builder helper
"""

from django.db import models
from seed.models.model import Model


class File(Model):

    url = models.URLField(
        max_length=1024, help_text="File reference link (eg. http://localhost:8000/image.png)")
    size = models.IntegerField(help_text="File size in bytes")
    name = models.CharField(
        max_length=1024, help_text="Common File Name (eg. Image.png)")

    class Meta:
        db_table = 'file'
        app_label = 'models'