"""
__Seed builder__
  (Read_only) Model helper
"""
import json

import jsonschema
from django.core import exceptions
from django.db import models

class JSONSchemaField(models.JSONField):

    def __init__(self, *args, **kwargs):
        self.schema = kwargs.pop('schema', None)
        super().__init__(*args, **kwargs)

    def _validate_schema(self, value):

        # Disable validation when migrations are faked
        if self.model.__module__ == '__fake__':
            return True

        # Ignore none values, these are validated in other module
        if value is None:
            return True

        try:
            if not isinstance(value, dict) and not isinstance(value, list):
                value = json.loads(str(value))
            jsonschema.validate(value, json.loads(self.schema))
        except jsonschema.exceptions.ValidationError:
            raise exceptions.ValidationError(f'{value} failed JSON schema :: Schema = {self.schema}')
        return True

    def validate(self, value, model_instance):
        super().validate(value, model_instance)
        self._validate_schema(value)

    def pre_save(self, model_instance, add):
        value = super().pre_save(model_instance, add)
        if value and not self.null:
            self._validate_schema(value)
        return value