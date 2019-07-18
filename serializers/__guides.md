# Serializers

Represents the model mappers to enable rest requests (aka. models to json).

## Table of content

-  [Guidelines](#guidelines)
-  [Example](#example)
-  [References](#references)
-  [Seed serializers](#seed-serializers)

## Guidelines

-  Use serializers only to add extra attributes of models
   -  For example: properties

## Example

```python
class TeamSerializer(_TeamSerializer):  #
    
    class Meta(_TeamSerializer.Meta):
        # Include extra field called 'complete_name'
        extra_fields = ('complete_name')
```

## References

- Serializer reference: [https://www.django-rest-framework.org/api-guide/serializers/](https://www.django-rest-framework.org/api-guide/serializers/)

## Seed serializers

-  [PlayerSerializer](../seed/serializers/player.py)
-  [TeamSerializer](../seed/serializers/team.py)
-  [UserSerializer](../seed/serializers/user.py)
-  [MatchSerializer](../seed/serializers/stats/match.py)
-  [ScoreSerializer](../seed/serializers/stats/score.py)

> To export a serializer use command \
> $ seed export -m serializers:model_name
