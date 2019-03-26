from django.db import models

from team.models import Team

class Player(models.Model):
    name = models.CharField(max_length=256)
    photo_url = models.CharField(max_length=512)
    team = models.ForeignKey(Team, related_name='players', null=True, on_delete=models.CASCADE)