
"""
__Seed builder__v1.0
  AUTO_GENERATED (Read only)
  Modify via builder
  
  Guidelines: 
    - Use template as base for test creation
    - Run with > python3 manage.py test domain/tests
    - References: https://docs.djangoproject.com/en/2.2/topics/testing/overview/#writing-tests
"""

from django.test import TestCase
from app.models import Player
from app.models import Team
from app.models import User
from app.models import Match
from app.models import Score

class Template(TestCase):  #

    def test(self):
        res = "hi!"
        self.assertEqual("hi!", res)
