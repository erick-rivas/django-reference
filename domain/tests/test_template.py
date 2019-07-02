"""
__Seed builder__v1.0
  Guidelines: 
    - Modify attributes via SeedManifest.yaml
    - Use template as base for domain creation
    - References: https://docs.djangoproject.com/en/2.2/topics/testing/overview/#writing-tests
"""

from django.test import TestCase

from models.user import User
from models.team import Team
from models.player import Player
from models.stats.match import Match
from models.stats.score import Score

class Test(TestCase):  #
    
    def setUp(self):
        pass # Tip: Create objects

    def test(self):
        pass
