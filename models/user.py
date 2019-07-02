"""
__Seed builder__v1.0

  Guidelines: 
    - Modify attributes via SeedManifest.yaml
    - Only add aggregate methods or definitions if required
      - Example: has_members(), complete_name() ...
    - Reference: https://docs.djangoproject.com/en/2.2/topics/db/models/#model-attributes

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

