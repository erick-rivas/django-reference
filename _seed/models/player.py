"""
__Seed builder__v1.0
  (Read_only) Modify via SeedManifest.yaml
"""

from datetime import datetime
from django.db import models
from models.helpers.model import Model

class _Player(Model):  #
    
    name = models.CharField(max_length=256, blank=True)
    photo = models.ForeignKey('File', related_name='player_photos', 
        blank=False, null=False, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    team = models.ForeignKey('Team', related_name='players', 
        blank=False, null=False, on_delete=models.CASCADE)

    class Meta:
        abstract = True

