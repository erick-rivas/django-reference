def _get(model, **values):
    try:
        return model.objects.get(**values)
    except model.DoesNotExist:
        return None

def _list(model, **values):
    return model.objects.filter(**values)

def _list_q(model, *values):
    return model.objects.filter(*values)

def _list_o(model, order_by, **values):
    return _list(model, **values).order_by(order_by)

def _queryset(model):
    return _list(model)

def _create(model, **values):
    return model.objects.create(**values)
