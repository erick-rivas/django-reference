"""
__Seed builder__v0.2.0
  (Read_only) Model permission util
"""

from seed.util.query_util import multi_q


def inherit_perms(parent_model, attr, user):
    """
    | Create a new permission collection in a specific attribute with parent_model perms
    | Example (Account, master_account) -> returns ["master_account__owner_id¨]

    :param parent_model: Parent model where get perms (ej. app.models.Account)
    :param attr: Child attribute to include parent perms
    :param user: User object
    :return: Permission collection with parent perms
    """
    permissions = parent_model.permission_filters(user)
    return _inherit_permissions_query(permissions, attr)


def _inherit_permissions_query(permissions, attr):
    if isinstance(permissions, dict):  # Single filter (ands)
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
    return queryset.filter(multi_q(filters))