"""
__Seed builder__v1.0

  Guidelines: 
    - Modify attributes via models.json
    - Only add aggregate methods if required
      - Example: has_members(), is_frequent_user() ...

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
