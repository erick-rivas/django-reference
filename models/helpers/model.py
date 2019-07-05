import time
import random
from django.db import models

class Model(models.Model):  #

    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    hash = models.CharField(max_length=32, default="", editable=False, null=True)

    def save(self, *args, **kwargs):
        pk = self.id
        if self.id is None:
            pk = random.randint(1, 100000)
        self.hash = hash((pk, time.time()))
        super().save(*args, **kwargs)

    class Meta:
        abstract = True
