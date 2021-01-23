from seed.util.query_util import multi_Q

def filter_perms(queryset, filters):
    if filters is None:
        return queryset
    return queryset.filter(multi_Q(filters))

def inherit_perms(model, attr, user):
    permissions = model.permission_filters(user)
    return inherit_permissions_query(permissions, attr)


def inherit_permissions_query(permissions, attr):
    if type(permissions) is dict:  # Single filter (ands)
        new_permissions = {}
        for key in permissions:
            new_permissions[attr + "__" + key] = permissions[key]
        return new_permissions
    else:  # Multiple filters (or, ands)
        new_permissions = []
        for permission in permissions:
            new_permissions.append(inherit_permissions_query(permission, attr))
        return new_permissions