"""
__Seed builder__v0.1.8
  (Read_only) Builder helper
"""

from dynamic_rest.serializers import DynamicModelSerializer

class Serializer(DynamicModelSerializer):
    class Meta:
        model = None
        exclude = None

def InnerSerializerClass(model):  #

    serializer = type('InnerSerializer', (Serializer,), {})
    meta = type('InnerMeta', (), {})
    meta.model = model
    serializer.Meta = meta
    return serializer

def InnerSerializer(model, **kargs):  #

    serializer_class = InnerSerializerClass(model)
    exclude = kargs.exclude if 'exclude' in kargs else []
    serializer_class.Meta.exclude = tuple(['created_at', 'updated_at'] + exclude)
    return serializer_class(**kargs)
