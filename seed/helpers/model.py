"""
__Seed builder__v0.1.8
  (Read_only) Builder helper
"""

import time
import random
from django.db import models

class Model(models.Model):  #

    created_at = models.DateTimeField(auto_now_add=True, null=True, help_text="Indicates the date on which the model was created")
    updated_at = models.DateTimeField(auto_now=True, null=True, help_text="Indicates the date it was last updated")
    hash = models.CharField(max_length=32, default="", editable=False, null=True, help_text="Unique identifier to identify the state of the model")

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

    class Meta:
        abstract = True
