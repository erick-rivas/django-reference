"""
__Seed builder__v0.1.8
  AUTO_GENERATED (Read only)
  Modify via builder
"""

from datetime import datetime
from django.contrib.auth.models import AbstractUser
from django.db import models
from seed.helpers.model import Model

class User(AbstractUser, Model):  #

    teams = models.ManyToManyField('models.Team', related_name='users', blank=False,
        db_table = '_user__teams', help_text="User team preferences")

    class Meta:
        db_table = '_user'
        app_label = 'models'