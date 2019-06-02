"""
__Seed builder__v1.0

  Guidelines: 
    - Modify attributes via models.json
    - Only add aggregate methods if required
      - Example: has_members(), is_frequent_user() ...

  Attributes:
    - id: int
    - teams: Team[]
"""

from django.db import models
from __seed__.models.user import _User

class User(_User):
    def __str__(self):
        return self.to_str('')
