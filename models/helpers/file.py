"""
__Seed builder__v1.0
  (Read_only) Builder helper
"""

import os
from datetime import datetime
from django.db import models
from seed.helpers.model import Model

class File(Model):  #

    url = models.URLField()
    size = models.IntegerField()
    name = models.CharField(max_length=128)
