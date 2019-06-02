"""
__Seed builder__v1.0

  Guidelines: 
    - Modify attributes via models.json
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
from __seed__.models.match import _Match

class Match(_Match):
    def __str__(self):
        return self.to_str('')
