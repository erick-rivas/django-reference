"""
__Seed builder__v0.2.0
  (Read_only) Builder helper
"""

import random
import time

from app.settings import get_env
from django.db import models
from django.db.models import Q


class Model(models.Model):
    created_at = models.DateTimeField(
        auto_now_add=True, null=True, help_text="Indicates the date on which the model was created")
    updated_at = models.DateTimeField(
        auto_now=True, null=True, help_text="Indicates the date it was last updated")
    hash = models.CharField(max_length=32, default="", editable=False, null=True,
                            help_text="Unique identifier to identify the state of the model")

    def save(self, *args, **kwargs):
        pk = self.id
        if self.id is None:
            pk = random.randint(1, 100000)
        self.hash = hash((pk, time.time()))
        super().save(*args, **kwargs)

    def get(self, **values):
        try:
            return self.objects.get(**values)
        except self.DoesNotExist:
            return None

    @staticmethod
    def filter_permissions(queryset, filters):
        if filters is None:
            return queryset
        if type(filters) is dict:  # Single filter (ands)
            return queryset.filter(**filters)
        else:  # Multiple filters (or, ands)
            query = Q()
            for filter in filters:
                query |= Q(**filter)
            return queryset.filter(query)

    @staticmethod
    def permission_filters(user):
        return None

    @staticmethod
    def inherit_permissions(model, attr, user):
        permissions = model.permission_filters(user)
        if type(permissions) is dict:  # Single filter (ands)
            new_permissions = {}
            for key in permissions:
                new_permissions[attr + "__" + key] = permissions[key]
            return new_permissions
        else:  # Multiple filters (or, ands)
            new_permissions = []
            for permission in permissions:
                new_permission = {}
                for key in permission:
                    new_permission[attr + "__" + key] = permission[key]
                new_permissions.append(new_permission)
            return new_permissions

    class Meta:
        abstract = True