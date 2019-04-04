class Util:

    @staticmethod
    def get_attr_list(model, *exclude):
        attrs = []
        fields = model._meta.get_fields()
        for field in fields:
            if not field.name in exclude:
                attrs.append(str(field.name))
        return tuple(attrs)
