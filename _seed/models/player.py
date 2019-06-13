"""
__Seed builder__v1.0
  (Read_only) Modify via models.json
"""

from datetime import datetime
from django.db import models
from models.helpers.model import Model

class _Player(Model):  #
    
    name = models.CharField(max_length=256)
    photo_url = models.CharField(max_length=512)
    is_active = models.BooleanField(default=True)
    team = models.ForeignKey('Team', related_name='players', 
        blank=False, null=False, on_delete=models.CASCADE)

    class Meta:
        abstract = True


