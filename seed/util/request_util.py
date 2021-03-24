"""
__Seed builder__v0.2.0
  (Read_only) Request util
"""

from rest_framework.exceptions import ValidationError


def has_fields_or_400(request_data, *required_fields):
    """
    Returns 400 exception if a field is missing in request

    :param request_data: Request data object
    :param required_fields: Array of required fields (Ex. [name, password])
    :return: 400 Exception if a required field is missing in request data
    """
    for field in required_fields:
        if field not in request_data:
            raise ValidationError()