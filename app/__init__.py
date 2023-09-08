"""
__Seed builder__
  AUTO_GENERATED Proxy (Read only)
  Modify via builder
"""

import importlib

import apipkg
apipkg.initpkg(__name__, {
    'models': {
        'Match': 'seed.models.match:Match',
        'Player': 'seed.models.player:Player',
        'PlayerPosition': 'seed.models.player_position:PlayerPosition',
        'Score': 'seed.models.score:Score',
        'Team': 'seed.models.team:Team',
        'User': 'seed.models.user:User',
        'File': 'seed.models.file:File',
    },
    'serializers': {
        'MatchSerializer': 'seed.serializers.match:MatchSerializer',
        'PlayerSerializer': 'seed.serializers.player:PlayerSerializer',
        'PlayerPositionSerializer': 'seed.serializers.player_position:PlayerPositionSerializer',
        'ScoreSerializer': 'seed.serializers.score:ScoreSerializer',
        'TeamSerializer': 'seed.serializers.team:TeamSerializer',
        'UserSerializer': 'seed.serializers.user:UserSerializer',
        'FileSerializer': 'seed.serializers.file:File',
    },
    'routes': {
        'MatchViewSet': 'seed.routes.matches:MatchViewSet',
        'PlayerViewSet': 'seed.routes.players:PlayerViewSet',
        'PlayerPositionViewSet': 'seed.routes.player_positions:PlayerPositionViewSet',
        'ScoreViewSet': 'seed.routes.scores:ScoreViewSet',
        'TeamViewSet': 'seed.routes.teams:TeamViewSet',
        'UserViewSet': 'seed.routes.users:UserViewSet',
        'FileView': 'seed.routes.files:FileView',
    },
})