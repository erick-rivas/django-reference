"""
__Seed builder__v1.0

  Base attributes:
    - id: int
    - name: string
"""

from django.db import models
from seed.models.player_type import _PlayerType

class PlayerType(_PlayerType):  #
    pass
