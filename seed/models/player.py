"""
__Seed builder__v0.2.0
  AUTO_GENERATED (Read only)
  Modify via builder
"""

from django.db import models
from seed.helpers.model import Model

class Player(Model):

    name = models.CharField(max_length=256, blank=True)
    photo = models.ForeignKey('models.File', related_name='player_photos',
        blank=False, null=False, on_delete=models.PROTECT)
    is_active = models.BooleanField(default=True, help_text="Indicates whether the player is active or retired" )

    team = models.ForeignKey('models.Team', related_name='players',
        blank=False, null=False, on_delete=models.CASCADE)
    position = models.ForeignKey('models.PlayerPosition', related_name='position_players',
        blank=False, null=False, on_delete=models.CASCADE)

    class Meta:
        db_table = '_player'
        app_label = 'models'
