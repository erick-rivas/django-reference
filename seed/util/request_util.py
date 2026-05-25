"""
__Seed builder__
  AUTO_GENERATED (Read only)
  Request util
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

def get_user_object_or_403(klass, user, *args, **kwargs):
    """
    Returns 404 exception if object doesn't exist or 403 if user doesn't have permissions

    :param klass: Model, Manager, or QuerySet object
    :param user: User model of the owner
    :param args: Arguments of the queryset
    :param kwargs: Keyword arguments of the queryset
    :return: 404 exception if object doesn't exist or 403 if user doesn't have permissions
    """
    from django.core.exceptions import PermissionDenied
    from seed.util.model_util import filter_perms

    get_object_or_404(klass, *args, **kwargs)
    queryset = filter_perms(klass.objects.filter(*args, **kwargs), klass.permission_filters(user)).first()
    if queryset is None:
        raise PermissionDenied("Unauthorized access to %s query." % queryset.model._meta.object_name)
    return queryset

def get_objects_by_pk_or_404(klass, pks):
    """
    Returns 404 exception if queryset don't have all the results based on pks,
    which means user doesn't have permissions for some objects

    :param klass: Model, Manager, or QuerySet object
    :param pks: Primary keys of the objects (E.g. [1, 2, 3])
    :return: 404 Exception if queryset don't have all the results based on pks
    """
    from django.http import Http404
    from django.db.models import Q

    pks = list(set(pks))  # Remove duplicates
    query = Q() if len(pks) > 0 else Q(pk__in=[])  # No pk case
    for pk in pks: query |= Q(pk=pk)

    queryset = klass.objects.filter(query)
    if queryset.count() != len(pks):
        raise Http404("No %s matches all the given query." % queryset.model._meta.object_name)
    return queryset

def get_user_objects_by_pk_or_403(klass, user, pks):
    """
    Returns 404 exception if queryset don't have all the results based on pks,
    or 403 if user doesn't have permissions for some objects.

    :param klass: Model, Manager, or QuerySet object
    :param user: User model of the owner
    :param pks: Primary keys of the objects (E.g. [1, 2, 3])
    :return: 404 exception if queryset don't have all the result or 403 if user doesn't have permissions
    """
    from django.core.exceptions import PermissionDenied
    from seed.util.model_util import filter_perms

    pks = list(set(pks))  # Remove duplicates
    base_queryset = get_objects_by_pk_or_404(klass, pks)
    queryset = filter_perms(base_queryset, klass.permission_filters(user))
    if queryset.count() != len(pks):
        raise PermissionDenied("Unauthorized access to %s query." % queryset.model._meta.object_name)
    return queryset