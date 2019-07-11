"""
__Seed builder__v1.0

  Guidelines: 
    - Only add aggregate methods or definitions if required
      - Example: has_members(), complete_name() ...
    - Reference: https://docs.djangoproject.com/en/2.2/topics/db/models/#model-attributes

  Base attributes:
    - id: int
    - name: string
    - photo: image
    - is_active: boolean
    - team: team
"""

from django.db import models
from seed.models.player import _Player

class Player(_Player):  #
    pass
