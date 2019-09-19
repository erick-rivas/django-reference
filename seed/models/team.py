"""
__Seed builder__v1.0
  AUTO_GENERATED (Read only)
  Modify via builder
"""

from datetime import datetime
from django.db import models
from seed.helpers.model import Model

class _Team(Model):  #

    name = models.CharField(max_length=256, blank=True)
    logo = models.ForeignKey('models.File', related_name='team_logos',
        blank=False, null=False, on_delete=models.PROTECT)
    description = models.TextField(blank=True, default="No description available")
    market_value = models.FloatField(default=0)
    identity_docs = models.ManyToManyField('models.File', related_name='team_identity_docses', blank=False)

    rival = models.ForeignKey('models.Team', related_name='rival_teams',
        blank=True, null=True, on_delete=models.CASCADE)
    
    @property
    def players(self):
        return self.players.all()

    class Meta:
        db_table = '_team'
        abstract = True