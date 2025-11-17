"""
__Seed builder__
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

def get_user_object_or_404(klass, user, *args, **kwargs):
    """
    Returns 404 exception if object doesn't exist or user doesn't have permissions

    :param klass: Model, Manager, or QuerySet object
    :param user: User model of the owner
    :param args: Arguments of the queryset
    :param kwargs: Keyword arguments of the queryset
    :return: 404 Exception if object doesn't exist or user doesn't have permissions
    """
    from django.http import Http404
    from seed.util.model_util import filter_perms
    result = filter_perms(klass.objects.filter(*args, **kwargs), klass.permission_filters(user)).first()
    if result is None:
        raise Http404("Object not found or unauthorized.")
    return result

def get_object_or_404(klass, *args, **kwargs):
    """
    Returns 404 exception if object doesn't exist

    :param klass: Model, Manager, or QuerySet object
    :param args: Arguments of the queryset
    :param kwargs: Keyword arguments of the queryset
    :return: 404 Exception if object doesn't exist
    """
    from django.shortcuts import get_object_or_404 as _get_object_or_404
    return _get_object_or_404(klass, *args, **kwargs)