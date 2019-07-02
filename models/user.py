"""
__Seed builder__v1.0

  Guidelines: 
    - Modify attributes via SeedManifest.yaml
    - Only add aggregate methods if required
      - Example: has_members(), is_frequent_user() ...

  Attributes:
    - id: int
    - username: string
    - first_name: string
    - last_name: string
    - email: string
    - is_active: boolean
    - teams: Team[]
"""

from django.db import models
from _seed.models.user import _User

class User(_User):  #
    pass
