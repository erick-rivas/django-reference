"""
__Seed builder__v1.0

  Base attributes:
    - id: int
    - name: string
    - logo: image
    - description: text
    - market_value: float
    - identity_docs: file[]
    - rival: team
"""

from django.db import models
from seed.models.team import _Team

class Team(_Team):  #
    pass
