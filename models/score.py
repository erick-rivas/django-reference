"""
__Seed builder__v1.0
  Attributes:
    - id: int
    - min: int
    - player: Player
    - match: Match
"""

from django.db import models
from __seed__.models.score import _Score

class Score(_Score):
    def __str__(self):
        return self.to_str('')
