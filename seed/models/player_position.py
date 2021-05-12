"""
__Seed builder__
  AUTO_GENERATED (Read only)
  Modify via builder
"""

from django.db import models
from seed.models.model import Model

class PlayerPosition(Model):

    name = models.CharField(max_length=256, blank=True)
    details = models.JSONField(
        blank=True, default=dict)

    class Meta:
        db_table = '_player_position'
        app_label = 'models'