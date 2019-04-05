from django.db import models
import uuid

class Model(models.Model):

    uuid = models.UUIDField(editable=False, null=False, blank=False, default=uuid.uuid4)

    def to_str(self, val):
        return str(val) + " (" + str(self.id) + ")"

    class Meta:
        abstract = True
