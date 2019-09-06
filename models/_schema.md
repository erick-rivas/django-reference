# Base models

## Table of content
-  [Match](#Match)
-  [Player](#Player)
-  [Score](#Score)
-  [Team](#Team)
-  [User](#User)

##  Match

-  Attributes:
   -  id: int
   -  date: date
   -  type: enum
   -  local: team
   -  visitor: team
   -  scores: score[]

-  Reference: [Match](../seed/models/match.py)

##  Player

-  Attributes:
   -  id: int
   -  name: string
   -  photo: image
   -  is_active: boolean
   -  team: team

-  Reference: [Player](../seed/models/player.py)

##  Score

-  Attributes:
   -  id: int
   -  min: int
   -  player: player
   -  match: match

-  Reference: [Score](../seed/models/score.py)

##  Team

-  Attributes:
   -  id: int
   -  name: string
   -  logo: image
   -  description: text
   -  market_value: float
   -  identity_docs: file[]
   -  rival: team
   -  players: player[]

-  Reference: [Team](../seed/models/team.py)

##  User

-  Attributes:
   -  id: int
   -  username: string
   -  first_name: string
   -  last_name: string
   -  email: string
   -  is_active: boolean
   -  teams: team[]

-  Reference: [User](../seed/models/user.py)
