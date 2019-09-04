"""
__Seed builder__v1.0

  Base attributes:
    - id: int
    - date: date
    - type: enum
    - local: team
    - visitor: team
    - scores: score[]
"""

from django.db import models
from seed.models.match import _Match

class Match(_Match):  #
    pass
