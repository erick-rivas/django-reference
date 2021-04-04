"""
__Seed builder__v0.2.0
  (Read_only) Builder helper
"""

import secrets
import time

from app.settings import get_env
from django.db import models
from seed.util.model_util import filter_perms
from seed.util.model_util import inherit_perms


class Model(models.Model):
    created_at = models.DateTimeField(
        auto_now_add=True, null=True, help_text="Indicates the date on which the model was created")
    updated_at = models.DateTimeField(
        auto_now=True, null=True, help_text="Indicates the date it was last updated")
    hash = models.CharField(max_length=32, default="", editable=False, null=True,
                            help_text="Unique identifier to identify the state of the model")

    # pylint: disable=W0221
    def save(self, *args, **kwargs):
        pk = self.id
        if self.id is None:
            pk = int(''.join(secrets.choice("0123456789") for i in range(9)))
        self.hash = hash((pk, time.time()))
        super().save(*args, **kwargs)

    def get(self, **values):
        try:
            return self.objects.get(**values)
        except self.DoesNotExist:
            return None

    @staticmethod
    def filter_permissions(queryset, filters):
        if get_env('ENABLE_AUTH'):
            return filter_perms(queryset, filters)
        return queryset

    @staticmethod
    def permission_filters(user):
        return None

    @staticmethod
    def inherit_permissions(model, attr, user):
        return inherit_perms(model, attr, user)

    class Meta:
        abstract = True