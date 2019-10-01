"""
__Seed builder__v1.0

  Base attributes:
    - id: int
    - name: string
"""

from django.db import models
from seed.models.player_position import _PlayerPosition

class PlayerPosition(_PlayerPosition):  #
    pass
