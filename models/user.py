"""
__Seed builder__v1.0
  Attributes:
    - id: int
    - teams: Team[]
"""

from django.db import models
from __seed__.models.user import _User

class User(_User):
    def __str__(self):
        return self.to_str('')
