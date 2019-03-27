from django.db import models

from models.team import Team

class Match(models.Model):
    date = models.DateTimeField()
    type = models.CharField(max_length=128)
    visitor = models.OneToOneField(Team, related_name='visitor', on_delete=models.CASCADE)
    local = models.OneToOneField(Team, related_name='local', on_delete=models.CASCADE)
