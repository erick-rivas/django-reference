"""
__Seed builder__v1.0

  Guidelines: 
    - Modify attributes via SeedManifest.yaml
    - Only add aggregate methods if required
      - Example: has_members(), is_frequent_user() ...

  Attributes:
    - id: int
    - name: string
    - logo_url: string
    - description: text
    - market_value: float
"""

from django.db import models
from _seed.models.team import _Team

class Team(_Team):
    pass
