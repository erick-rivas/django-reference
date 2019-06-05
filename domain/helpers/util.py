def get(model, **values):
    return model.objects.filter(**values)

def get_o(model, order_by, **values):
    return get(model, **values).order_by(order_by)

def create(model, **values):
    return model.objects.create(**values)