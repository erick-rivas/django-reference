"""
__Seed builder__
  AUTO_GENERATED (Read only)
  Modify via builder
"""

from django.db import models
from seed.models.model import Model
from seed.models.helpers.json_schema_field import JSONSchemaField

class Team(Model):

    name = models.CharField(max_length=256,
        blank=True, null=False)
    logo = models.ForeignKey(
        'models.File', related_name='team_logos',
        blank=False, null=False, on_delete=models.PROTECT)
    description = models.TextField(
        blank=True, null=False, default="No description available")
    market_value = models.FloatField(
        default=0, help_text="Market value of the team in USD")
    identity_docs = models.ManyToManyField(
        'models.File', related_name='team_identity_docses', blank=False
        , help_text="Documents to indentify the team (constitutive act, registration, etc.)")

    rival = models.ForeignKey(
        'models.Team', related_name='rival_teams',
        blank=True, null=True, on_delete=models.CASCADE, help_text="Team's biggest rival")
    
    @property
    def players(self):
        return self.players.all()

    class Meta:
        db_table = '_team'
        app_label = 'models'