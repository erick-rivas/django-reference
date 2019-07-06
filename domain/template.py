"""
__Seed builder__v1.0
  (Read_only) Modify via SeedManifest.yaml
  
  Guidelines: 
    - Modify attributes via SeedManifest.yaml
    - Use template as base for domain creation
    - References:
        - Queries: https://docs.djangoproject.com/en/2.2/topics/db/queries/
"""

from django.db.models import Q
from domain.helpers.query_util import _get, _list, _list_q, _list_o, _queryset, _create

from models.player import Player
from models.team import Team
from models.user import User
from models.stats.match import Match
from models.stats.score import Score

def use_case_name():  #
    pass