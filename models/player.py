"""
__Seed builder__v1.0

  Guidelines: 
    - Modify attributes via SeedManifest.yaml
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
from _seed.models.player import _Player

class Player(_Player):
    pass
