# Models

Represents the model definitions of the application (database)

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

The model module represents the application models that define the database structure, it includes:
-  Data types
-  Foreign keys
-  Enums
-  Table settings

## Guidelines

-  Modify attributes types and names via builder.
-  Only add aggregate methods (properties) if required
   -  Example: has_members(), complete_name() ...

## Example

```python
class User(_User):  #

    @property
    def full_name(self):
        return self.first_name + " " self.last_name
```

## References

-  Model reference: [https://docs.djangoproject.com/en/2.2/topics/db/models/](https://docs.djangoproject.com/en/2.2/topics/db/models/)

## Seed models

###  Player

Reference: [Player](../seed/models/player.py) \
Attributes:
-  name
-  photo
-  is_active
-  team

###  Team

Reference: [Team](../seed/models/team.py) \
Attributes:
-  name
-  logo
-  description
-  market_value
-  rival
-  identity_docs
-  players

###  User

Reference: [User](../seed/models/user.py) \
Attributes:
-  teams

###  Match

Reference: [Match](../seed/models/stats/match.py) \
Attributes:
-  date
-  type
-  local
-  visitor
-  scores

###  Score

Reference: [Score](../seed/models/stats/score.py) \
Attributes:
-  min
-  player
-  match

> To export a model use command \
> $ seed export -m models:model_name
