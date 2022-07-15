"""
__Seed builder__
  (Read_only) Model base class
"""

import secrets
import time

from app.settings import get_env
from django.db import models
from django.db.models import Lookup
from django.db.models import Field

from seed.util.model_util import filter_perms
from seed.util.model_util import inherit_perms


class NotEqual(Lookup):
    lookup_name = 'ne'

    def as_sql(self, compiler, connection):
        lhs, lhs_params = self.process_lhs(compiler, connection)
        rhs, rhs_params = self.process_rhs(compiler, connection)
        params = lhs_params + rhs_params
        return '%s <> %s' % (lhs, rhs), params


class Model(models.Model):
    created_at = models.DateTimeField(
        auto_now_add=True, null=True, help_text="Indicates the date on which the model was created")
    updated_at = models.DateTimeField(
        auto_now=True, null=True, help_text="Indicates the date it was last updated")
    hash = models.CharField(max_length=32, default="", editable=False, null=True,
                            help_text="Unique identifier to identify the state of the model")
    Field.register_lookup(NotEqual)

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


class ModelRails(models.Model):
    created_at = models.DateTimeField(
        auto_now_add=True, null=True, help_text="Indicates the date on which the model was created")
    updated_at = models.DateTimeField(
        auto_now=True, null=True, help_text="Indicates the date it was last updated")

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