"""
__Seed builder__v1.0
"""

from datetime import datetime
from django.db import models
from models.helpers.model import Model

class _Team(Model):  #
    
    name = models.CharField(max_length=256)
    logo_url = models.CharField(max_length=512)
    description = models.TextField()
    market_value = models.FloatField()

    class Meta:
        abstract = True


