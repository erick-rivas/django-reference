"""
__Seed builder__v0.1.8
  AUTO_GENERATED (Read only)
  Modify via builder
"""

from datetime import datetime
from django.db import models
from seed.helpers.model import Model

class PlayerPosition(Model):  #

    name = models.CharField(max_length=256, blank=True)

    class Meta:
        db_table = '_player_position'
        app_label = 'models'
