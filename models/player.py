from django.db import models

from models.helpers.model import Model
from models.team import Team

class Player(Model):
    name = models.CharField(max_length=256)
    photo_url = models.CharField(max_length=512)
    team = models.ForeignKey(Team, related_name='players', blank=False, null=False, on_delete=models.CASCADE)

    def __str__(self):
        return self.to_str(self.name)
