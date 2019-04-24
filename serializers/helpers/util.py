class Util:

    @staticmethod
    def get_attr_list(model, exclude=(), include=()):
        attrs = []
        fields = model._meta.get_fields()
        for field in fields:
            if not field.name in exclude:
                attrs.append(str(field.name))
        for inc in include:
            attrs.append(str(inc))
        return tuple(attrs)
