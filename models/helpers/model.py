from django.db import models

class Model(models.Model):

    def to_str(self, val):
        return str(val) + " (" + str(self.id) + ")"

    class Meta:
        abstract = True
