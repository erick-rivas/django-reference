from django.db import models

from models.model import Model
from models.player import Player
from models.match import Match

class Score(Model):
    min = models.IntegerField()
    player = models.ForeignKey(Player, related_name='scores', blank=False, null=False, on_delete=models.CASCADE)
    match = models.ForeignKey(Match, related_name='scores', blank=False, null=False, on_delete=models.CASCADE)

    def __str__(self):
        return self.to_str("Min " + str(self.min) + self.match.__str__())
