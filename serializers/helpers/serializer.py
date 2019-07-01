from rest_framework import serializers

class Serializer(serializers.ModelSerializer):
    class Meta:
        model = None
        exclude = None

def InnerSerializer(model, **kargs):  #

    exclude = kargs.exclude if 'exclude' in kargs else []
    serializer = type('InnerSerializer', (Serializer, ), {})
    meta = type('InnerMeta', (), {})
    meta.model = model
    meta.exclude = tuple(['created_at', 'updated_at'] + exclude)
    serializer.Meta = meta
    return serializer(**kargs)
