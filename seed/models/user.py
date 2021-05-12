"""
__Seed builder__
  AUTO_GENERATED (Read only)
  Modify via builder
"""

from django.contrib.auth.models import AbstractUser
from django.db import models
from seed.models.model import Model

class User(AbstractUser, Model):

    profile_image = models.ForeignKey(
        'models.File', related_name='user_profile_images',
        blank=False, null=False, on_delete=models.PROTECT)

    teams = models.ManyToManyField(
        'models.Team', related_name='users', blank=False,
        db_table='_user__teams', help_text="User team preferences")

    class Meta:
        db_table = '_user'
        app_label = 'models'