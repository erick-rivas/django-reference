"""
__Seed builder__v0.2.0
  AUTO_GENERATED (Read only)
  Modify via builder
"""

from datetime import datetime
from django.db import models
from seed.models.model import Model

class Match(Model):
    
    TYPES = (
        ('FRIENDSHIP', 'Friendship'),
        ('LEAGUE', 'League'),
        ('CUP', 'Cup'),
    )

    date = models.DateTimeField(
        blank=False, null=False, default=datetime.now)
    type = models.CharField(max_length=64, choices=TYPES,
        blank=False, help_text="Match type (eg. cup)")

    local = models.ForeignKey('models.Team', related_name='local_matches',
        blank=False, null=False, on_delete=models.CASCADE)
    visitor = models.ForeignKey('models.Team', related_name='visitor_matches',
        blank=False, null=False, on_delete=models.CASCADE)
    
    @property
    def scores(self):
        return self.scores.all()

    class Meta:
        db_table = '_match'
        app_label = 'models'