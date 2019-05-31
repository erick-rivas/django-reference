"""
__Seed builder__v1.0
  Attributes:
    - id: int
    - name: string
    - photo_url: string
    - is_active: boolean
    - team: Team
"""

from django.db import models
from __seed__.models.player import _Player

class Player(_Player):
    def __str__(self):
        return self.to_str('')
