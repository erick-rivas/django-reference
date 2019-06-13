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
from _seed.models.user import _User

class User(_User):
    pass
