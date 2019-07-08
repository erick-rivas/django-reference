"""
__Seed builder__v1.0
  (Read_only) Modify via SeedManifest.yaml
"""

from datetime import datetime
from django.contrib.auth.models import AbstractUser
from django.db import models
from sbuild.helpers.model import Model

class _User(AbstractUser, Model):  #

    teams = models.ManyToManyField('Team', related_name='users', blank=False)

    class Meta:
        abstract = True
