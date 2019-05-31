"""
__Seed builder__v1.0
  Models:
    - User
    - Team
    - Player
    - Match
    - Score
"""

from django.contrib import admin
from __seed__.models.admin import _Admin

_Admin().register()