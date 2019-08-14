"""
__Seed builder__v1.0
  AUTO_GENERATED (Read only)
  Modify via builder
"""

from datetime import datetime
from django.db import models
from seed.helpers.model import Model

class _Match(Model):  #
    
    TYPES = (
        ('FRIENDSHIP', 'Friendship'),
        ('LEAGUE', 'League'),
        ('CUP', 'Cup'),
    )

    date = models.DateTimeField(default=datetime.now)
    type = models.CharField(max_length=32, choices=TYPES)

    local = models.ForeignKey('models.Team', related_name='local_matches',
        blank=False, null=False, on_delete=models.CASCADE)
    visitor = models.ForeignKey('models.Team', related_name='visitor_matches',
        blank=False, null=False, on_delete=models.CASCADE)
    
    @property
    def scores(self):
        return self.scores.all()

    class Meta:
        db_table = '_match'
        abstract = True
