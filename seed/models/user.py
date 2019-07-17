"""
__Seed builder__v1.0
  AUTO_GENERATED (Read only)
  Modify via builder
"""

from datetime import datetime
from django.contrib.auth.models import AbstractUser
from django.db import models
from seed.helpers.model import Model

class _User(AbstractUser, Model):  #

    teams = models.ManyToManyField('models.Team', related_name='users', blank=False)

    class Meta:
        db_table = 'user'
        abstract = True
