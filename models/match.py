"""
__Seed builder__v1.0

  Guidelines: 
    - Modify attributes via SeedManifest.yaml
    - Only add aggregate methods if required
      - Example: has_members(), is_frequent_user() ...

  Attributes:
    - id: int
    - date: date
    - type: enum
    - local: Team
    - visitor: Team
"""

from django.db import models
from _seed.models.match import _Match

class Match(_Match):  #
    pass
