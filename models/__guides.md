# Models

Represents the model definitions of the application (database)

## Table of content

-  [Description](#description)
-  [Guidelines](#guidelines)
-  [Example](#example)
-  [References](#references)
-  [Seed models](#seed-models)
    -  [Match](#Match)
    -  [Player](#Player)
    -  [Score](#Score)
    -  [Team](#Team)
    -  [User](#User)

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
        return self.first_name + " " + self.last_name
```

## References

-  Model reference: [https://docs.djangoproject.com/en/2.2/topics/db/models/](https://docs.djangoproject.com/en/2.2/topics/db/models/)

## Seed models

###  Match

Reference: [Match](../seed/models/match.py) \
Attributes:
-  id: int
-  date: date
-  type: enum
-  local: team
-  visitor: team
-  scores: score[]

###  Player

Reference: [Player](../seed/models/player.py) \
Attributes:
-  id: int
-  name: string
-  photo: image
-  is_active: boolean
-  team: team

###  Score

Reference: [Score](../seed/models/score.py) \
Attributes:
-  id: int
-  min: int
-  player: player
-  match: match

###  Team

Reference: [Team](../seed/models/team.py) \
Attributes:
-  id: int
-  name: string
-  logo: image
-  description: text
-  market_value: float
-  identity_docs: file[]
-  rival: team
-  players: player[]

###  User

Reference: [User](../seed/models/user.py) \
Attributes:
-  id: int
-  username: string
-  first_name: string
-  last_name: string
-  email: string
-  is_active: boolean
-  teams: team[]

> To export a model use command \
> $ seed export -m models:model_name
