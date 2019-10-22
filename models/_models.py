
"""
__Seed builder__v0.1.8
  AUTO_GENERATED (Use seed-builder to modify)

- Match
   -  id: int
   -  date: date
   -  type: enum
   -  local: team
   -  visitor: team
   -  scores: score[]

- Player
   -  id: int
   -  name: string
   -  photo: image
   -  is_active: boolean
   -  team: team
   -  position: player_position

- PlayerPosition
   -  id: int
   -  name: string

- Score
   -  id: int
   -  min: int
   -  player: player
   -  match: match

- Team
   -  id: int
   -  name: string
   -  logo: image
   -  description: text
   -  market_value: float
   -  identity_docs: file[]
   -  rival: team
   -  players: player[]

- User
   -  id: int
   -  username: string
   -  first_name: string
   -  last_name: string
   -  email: string
   -  is_active: boolean
   -  teams: team[]
"""

