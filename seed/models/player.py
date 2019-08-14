"""
__Seed builder__v1.0
  AUTO_GENERATED (Read only)
  Modify via builder
"""

from datetime import datetime
from django.db import models
from seed.helpers.model import Model

class _Player(Model):  #

    name = models.CharField(max_length=256, blank=True)
    photo = models.ForeignKey('models.File', related_name='player_photos',
        blank=False, null=False, on_delete=models.PROTECT)
    is_active = models.BooleanField(default=True)

    team = models.ForeignKey('models.Team', related_name='players',
        blank=False, null=False, on_delete=models.CASCADE)

    class Meta:
        db_table = '_player'
        abstract = True
