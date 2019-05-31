"""
__Seed builder__v1.0
"""

from datetime import datetime
from django.db import models
from models.helpers.model import Model

class _Match(Model):  #
    
    TYPES = (
        ('FRIENDSHIP', 'Friendship'),
        ('LEAGUE', 'League'),
        ('CUP', 'Cup'),
    )
    date = models.DateTimeField(default=datetime.now)
    type = models.CharField(max_length=32, choices=TYPES)
    local = models.ForeignKey('Team', related_name='local_matches', 
        blank=False, null=False, on_delete=models.CASCADE)
    visitor = models.ForeignKey('Team', related_name='visitor_matches', 
        blank=False, null=False, on_delete=models.CASCADE)

    class Meta:
        abstract = True


