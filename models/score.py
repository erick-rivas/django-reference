"""
__Seed builder__v1.0

  Base attributes:
    - id: int
    - min: int
    - player: player
    - match: match
"""

from django.db import models
from seed.models.score import _Score

class Score(_Score):  #
    pass
