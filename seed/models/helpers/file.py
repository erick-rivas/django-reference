"""
__Seed builder__v1.0
  (Read_only) Builder helper
"""

import os
from datetime import datetime
from django.db import models
from seed.helpers.model import Model

class File(Model):  #

    url = models.URLField(max_length=1024)
    size = models.IntegerField()
    name = models.CharField(max_length=1024)

    class Meta:
        db_table = 'file'
        app_label = 'models'
