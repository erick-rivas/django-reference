"""
__Seed builder__v1.0

  Guidelines: 
    - Only add aggregate methods or definitions if required
      - Example: has_members(), complete_name() ...
    - Reference: https://docs.djangoproject.com/en/2.2/topics/db/models/#model-attributes

  Base attributes:
    - id: int
    - date: date
    - type: enum
    - local: team
    - visitor: team
"""

from django.db import models
from seed.models.stats.match import _Match

class Match(_Match):  #
    pass
