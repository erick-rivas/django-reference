"""
__Seed builder__v0.1.8
  (Read_only) Builder helper
"""

from rest_framework.exceptions import ValidationError

def has_fields_or_400(data, *required_fields):
    for field in required_fields:
        if field not in data:
            raise ValidationError()
