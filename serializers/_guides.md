# Serializers

Represents the model mappers to enable rest requests (aka. models to json).

## Table of content

-  [Guidelines](#guidelines)
-  [Example](#example)
-  [References](#references)

## Guidelines

-  Use serializers only to add extra attributes of models
   -  For example: properties
-  To export a serializer use command \
>  $ seed export -m serializers:model_name

## Example

```python
class TeamSerializer(_TeamSerializer):  #
    
    class Meta(_TeamSerializer.Meta):
        # Include extra field called 'complete_name'
        extra_fields = ('complete_name',)
        fields = _TeamSerializer.Meta.fields + extra_fields
```

## References

- Serializer reference: [https://www.django-rest-framework.org/api-guide/serializers/](https://www.django-rest-framework.org/api-guide/serializers/)
