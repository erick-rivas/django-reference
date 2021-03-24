# Serializers

Represents the model mappers to REST outputs (e.g. models to json)


## Example

```python
class TeamSerializer(_TeamSerializer):
    
    class Meta(_TeamSerializer.Meta):
        # Include extra field called 'complete_name'
        extra_fields = ('complete_name',)
        fields = _TeamSerializer.Meta.fields + extra_fields
```

## Guidelines

-   Use serializers only to add extra attributes of models
    -   For example: properties

## References

-   Serializer reference: [https://www.django-rest-framework.org/api-guide/serializers/](https://www.django-rest-framework.org/api-guide/serializers/)