# Models

Represents the model definitions to database

## Table of content

-  [Description](#description)
-  [Guidelines](#guidelines)
-  [Example](#example)
-  [References](#references)
-  [Seed models](#seed-models)
    -  [Player](#Player)
    -  [Team](#Team)
    -  [User](#User)
    -  [Match](#Match)
    -  [Score](#Score)

## Description

The model module represents the application models that define the database structure.

## Guidelines

-  Only add aggregate methods or definitions if required
   -  Example: has_members(), complete_name() ...

## Example

```python
class Player(_Player):  #
    pass
```

## References

-  Model reference: [https://docs.djangoproject.com/en/2.1/topics/db/models/](https://docs.djangoproject.com/en/2.1/topics/db/models/)

## Seed models

###  Player

Reference: [Player](../seed/serializers/player.py) \
Attributes:
-  name
-  photo
-  is_active
-  team

###  Team

Reference: [Team](../seed/serializers/team.py) \
Attributes:
-  name
-  logo
-  description
-  market_value
-  rival
-  identity_docs
-  players

###  User

Reference: [User](../seed/serializers/user.py) \
Attributes:
-  teams

###  Match

Reference: [Match](../seed/serializers/stats/match.py) \
Attributes:
-  date
-  type
-  local
-  visitor
-  scores

###  Score

Reference: [Score](../seed/serializers/stats/score.py) \
Attributes:
-  min
-  player
-  match
