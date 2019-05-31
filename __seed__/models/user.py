"""
__Seed builder__v1.0
"""

from datetime import datetime
from django.contrib.auth.models import AbstractUser
from django.db import models
from models.helpers.model import Model

class _User(AbstractUser):  #
    
    teams = models.ManyToManyField('Team', related_name='users', blank=False)

    class Meta:
        abstract = True


