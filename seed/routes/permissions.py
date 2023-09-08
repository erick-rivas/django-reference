"""
__Seed builder__
  (Read_only) Routes helper
"""
from rest_framework.permissions import BasePermission

class IsDevUser(BasePermission):
    """
    Allows access only to developer users.
    """

    def has_permission(self, request, view):
        # TODO CHECK
        return bool(request.user and request.user.is_superuser)