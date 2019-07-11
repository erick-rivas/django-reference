"""
__Seed builder__v1.0
  AUTO_GENERATED (Read only)
  Modify via builder
"""

def get_player_serializer():
    try:
        from serializers.player import PlayerSerializer
        return PlayerSerializer
    except:
        from seed.serializers.player import _PlayerSerializer
        return _PlayerSerializer

def get_team_serializer():
    try:
        from serializers.team import TeamSerializer
        return TeamSerializer
    except:
        from seed.serializers.team import _TeamSerializer
        return _TeamSerializer

def get_user_serializer():
    try:
        from serializers.user import UserSerializer
        return UserSerializer
    except:
        from seed.serializers.user import _UserSerializer
        return _UserSerializer

def get_match_serializer():
    try:
        from serializers.stats.match import MatchSerializer
        return MatchSerializer
    except:
        from seed.serializers.stats.match import _MatchSerializer
        return _MatchSerializer

def get_score_serializer():
    try:
        from serializers.stats.score import ScoreSerializer
        return ScoreSerializer
    except:
        from seed.serializers.stats.score import _ScoreSerializer
        return _ScoreSerializer

def get_file_serializer():
    from seed.serializers.helpers.file import FileSerializer
    return FileSerializer

PlayerSerializer = get_player_serializer()
TeamSerializer = get_team_serializer()
UserSerializer = get_user_serializer()
MatchSerializer = get_match_serializer()
ScoreSerializer = get_score_serializer()
FileSerializer = get_file_serializer()