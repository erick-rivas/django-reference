"""
__Seed builder__v0.2.0
  (Read_only) Model permission util
"""

from seed.util.query_util import multi_Q


def inherit_perms(parent_model, attr, user):
    """
    Create a new permission collection in an specific attribute with parent_model perms
    Ex. (Account, master_account) -> returs ["master_account__owner_id¨] // In case Account Model has owner_id as perms

    :param parent_model: Parent model where get perms (ej. app.models.Account)
    :param attr: Child attribute to include parent perms
    :param user: User object
    :return: Permission collection with parent perms
    """
    permissions = parent_model.permission_filters(user)
    return _inherit_permissions_query(permissions, attr)


def _inherit_permissions_query(permissions, attr):
    if type(permissions) is dict:  # Single filter (ands)
        new_permissions = {}
        for key in permissions:
            new_permissions[attr + "__" + key] = permissions[key]
        return new_permissions
    else:  # Multiple filters (or, ands)
        new_permissions = []
        for permission in permissions:
            new_permissions.append(_inherit_permissions_query(permission, attr))
        return new_permissions


def filter_perms(queryset, filters):
    """
    Execute queryset filtering based on model perms

    :param queryset: Model queryset
    :param filters: Filter collection
    :return: Queryset filtered
    """
    if filters is None:
        return queryset
    return queryset.filter(multi_Q(filters))