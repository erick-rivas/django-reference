"""
__Seed builder__v1.0
  AUTO_GENERATED (Read only)
  Modify via builder
"""

def get_match():
    from models.match import Match
    return Match

def get_player():
    from models.player import Player
    return Player

def get_player_position():
    from models.player_position import PlayerPosition
    return PlayerPosition

def get_score():
    from models.score import Score
    return Score

def get_team():
    from models.team import Team
    return Team

def get_user():
    from models.user import User
    return User

def get_file():
    from seed.models.helpers.file import File
    return File

Match = get_match()
Player = get_player()
PlayerPosition = get_player_position()
Score = get_score()
Team = get_team()
User = get_user()
File = get_file()
