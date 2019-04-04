from django.db import models

from models.helpers.model import Model
from models.team import Team

class Match(Model):
    TYPES = (
        ('F', 'Friendship'),
        ('C', 'Cup'),
        ('L', 'League')
    )
    date = models.DateTimeField()
    type = models.CharField(max_length=8, choices=TYPES)
    visitor = models.ForeignKey(Team, related_name='visitors', blank=False, null=False, on_delete=models.CASCADE)
    local = models.ForeignKey(Team, related_name='locals', blank=False, null=False, on_delete=models.CASCADE)

    def __str__(self):
        return self.to_str(self.local.name + " vs " + self.visitor.name)