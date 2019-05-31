"""
__Seed builder__v1.0
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
