"""
__Seed builder__v1.0

  Guidelines: 
    - Modify attributes via SeedManifest.yaml
    - Only add aggregate methods or definitions if required
      - Example: has_members(), complete_name() ...
    - Reference: https://docs.djangoproject.com/en/2.2/topics/db/models/#model-attributes

  Attributes:
    - id: int
    - name: string
    - logo: image
    - description: text
    - market_value: float
    - identity_docs: file[]
"""

from django.db import models
from _seed.models.team import _Team

class Team(_Team):  #
    pass
