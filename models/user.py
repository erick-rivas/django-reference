"""
__Seed builder__v1.0

  Base attributes:
    - id: int
    - username: string
    - first_name: string
    - last_name: string
    - email: string
    - is_active: boolean
    - teams: team[]
"""

from django.db import models
from seed.models.user import _User

class User(_User):  #
    pass
