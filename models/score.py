"""
__Seed builder__v1.0

  Guidelines: 
    - Modify attributes via SeedManifest.yaml
    - Only add aggregate methods if required
      - Example: has_members(), is_frequent_user() ...

  Attributes:
    - id: int
    - min: int
    - player: Player
    - match: Match
"""

from django.db import models
from _seed.models.score import _Score

class Score(_Score):
    pass
