"""
__Seed builder__v1.0

  Guidelines: 
    - Modify attributes via SeedManifest.yaml
    - Only add aggregate methods or definitions if required
      - Example: has_members(), complete_name() ...
    - Reference: https://docs.djangoproject.com/en/2.2/topics/db/models/#model-attributes

  Attributes:
    - id: int
    - date: date
    - type: enum
    - local: Team
    - visitor: Team
"""

from django.db import models
from sbuild.models.stat.match import _Match

class Match(_Match):  #
    pass
