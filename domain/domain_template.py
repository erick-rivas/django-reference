"""
__Seed builder__v1.0
  Guidelines: 
    - Modify attributes via SeedManifest.yaml
    - Use template as base for domain creation
    - References:
        - Queries: https://docs.djangoproject.com/en/2.2/topics/db/queries/
"""

from domain.helpers.query_util import _get, _list, _list_q, _list_o, _queryset, _create

from models.stats.match import Match
from models.player import Player
from models.stats.score import Score
from models.team import Team
from models.user import User

def use_case_name():  #
    pass