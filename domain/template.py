"""
__Seed builder__v1.0
  AUTO_GENERATED (Read only)
  Modify via builder
  
  Guidelines: 
    - Use template as base for domain creation
    - References:
      - Queries: https://docs.djangoproject.com/en/2.2/topics/db/queries/
"""

from django.db.models import Q
from seed.util.query_util import _get, _list, _list_q, _list_o, _queryset, _create

from app.models import Player
from app.models import Team
from app.models import User
from app.models import Match
from app.models import Score

def use_case_name():  #
    pass