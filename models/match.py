"""
__Seed builder__v1.0
  Attributes:
    - id: int
    - date: date
    - type: enum
    - local: Team
    - visitor: Team
"""

from django.db import models
from __seed__.models.match import _Match

class Match(_Match):
    def __str__(self):
        return self.to_str('')
