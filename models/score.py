from django.db import models

from models.player import Player

from models.match import Match

class Score(models.Model):
    min = models.IntegerField()
    player = models.OneToOneField(Player, related_name='player', on_delete=models.CASCADE)
    match = models.ForeignKey(Match, related_name='scores', null=True, on_delete=models.CASCADE)
