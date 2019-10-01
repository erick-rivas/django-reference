"""
__Seed builder__v1.0
  AUTO_GENERATED (Read only)
  Modify via builder
"""

from datetime import datetime
from django.db import models
from seed.helpers.model import Model

class _Score(Model):  #

    min = models.IntegerField(default=0, help_text="Minute of the goal")

    player = models.ForeignKey('models.Player', related_name='scores',
        blank=False, null=False, on_delete=models.CASCADE, help_text="Player that score")
    match = models.ForeignKey('models.Match', related_name='scores',
        blank=False, null=False, on_delete=models.CASCADE)

    class Meta:
        db_table = '_score'
        abstract = True
