"""
__Seed builder__v1.0

  Guidelines: 
    - Modify attributes via models.json
    - Only add aggregate methods if required
      - Example: has_members(), is_frequent_user() ...

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
