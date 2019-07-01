"""
__Seed builder__v1.0
  (Read_only) Modify via SeedManifest.yaml
"""

from datetime import datetime
from django.contrib.auth.models import AbstractUser
from django.db import models
from models.helpers.model import Model

class _User(AbstractUser, Model):  #
    
    teams = models.ManyToManyField('Team', related_name='users', blank=False)
    profile_image = models.ForeignKey('File', related_name='user_profile_images', 
        blank=False, null=False, on_delete=models.CASCADE)

    class Meta:
        abstract = True

