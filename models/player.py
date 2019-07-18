"""
__Seed builder__v1.0

  Base attributes:
    - id: int
    - name: string
    - photo: image
    - is_active: boolean
    - team: team
"""

from django.db import models
from seed.models.player import _Player

class Player(_Player):  #
    pass
