"""
__Seed builder__v1.0

  Guidelines: 
    - Modify attributes via models.json
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
from __seed__.models.team import _Team

class Team(_Team):
    def __str__(self):
        return self.to_str('')
