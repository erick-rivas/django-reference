from django.db import models
from datetime import datetime

class Model(models.Model):  #

    created_at = models.DateTimeField(default=datetime.now)

    def to_str(self, val):
        return str(val) + " (" + str(self.id) + ")"

    class Meta:
        abstract = True
