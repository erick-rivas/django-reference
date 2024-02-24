"""
__Seed builder__
  AUTO_GENERATED (Read only)
  Modify via builder
"""

from django.db import models
from seed.models.model import Model
from seed.models.helpers.json_schema_field import JSONSchemaField

class PlayerPosition(Model):

    name = models.CharField(max_length=256,
        blank=True, null=False)
    code = models.TextField(
        blank=True, null=False)
    # pylint: disable=C0301
    stats = JSONSchemaField(
        blank=True, null=False, default=dict,
        schema=""" {"type":"object","properties":{"expected_goals":{"type":"number"},"dominant_leg":{"type":"string"},"dominant_leg_accuracy":{"type":"number"}},"required":["expected_goals"],"dependentRequired":{"dominant_leg_accuracy":["dominant_leg_accuracy"]}} """
    )
    # pylint: disable=C0301
    details = JSONSchemaField(
        blank=True, null=False, default=dict,
        schema=""" {} """
    )

    class Meta:
        db_table = '_player_position'
        app_label = 'models'