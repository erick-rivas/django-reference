"""
__Seed builder__
  AUTO_GENERATED (Read only)
  Modify via builder
"""

from django.utils import timezone
from django.db import models
from seed.models.model import Model

class Match(Model):
    
    TYPES = (
        ('FRIENDSHIP', 'Friendship'),
        ('LEAGUE', 'League'),
        ('CUP', 'Cup'),
    )

    date = models.DateTimeField(
        blank=False, null=False, default=timezone.now)
    type = models.CharField(
        max_length=64, choices=TYPES,
        blank=False, null=False, help_text="Match type (eg. cup)")

    local = models.ForeignKey(
        'models.Team', related_name='local_matches',
        blank=False, null=False,
        on_delete=models.CASCADE)
    visitor = models.ForeignKey(
        'models.Team', related_name='visitor_matches',
        blank=False, null=False,
        on_delete=models.CASCADE)
    
    @property
    def scores(self):
        return self.scores.all()

    class Meta:
        db_table = '_match'
        app_label = 'models'