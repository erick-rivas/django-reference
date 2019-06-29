"""
__Seed builder__v1.0
  (Read_only) Modify via SeedManifest.yaml
"""

from datetime import datetime
from django.db import models
from models.helpers.model import Model

class _Team(Model):  #
    
    name = models.CharField(max_length=256, blank=True)
    logo_url = models.CharField(max_length=512, blank=True)
    description = models.TextField(blank=True, default="No description available")
    market_value = models.FloatField()

    class Meta:
        abstract = True

