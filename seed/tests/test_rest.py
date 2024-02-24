"""
__Seed builder__
  AUTO_GENERATED (Read only)
  Modify via builder
"""

import json
from rest_framework import status
from rest_framework.test import APITestCase
from seed.util.test_util import fill_test_database
from dj_rest_auth.models import TokenModel
from app.models import User

class TestRest(APITestCase):
    def setUp(self):
        fill_test_database()
        user = User.objects.all().first()
        token, created = TokenModel.objects.get_or_create(user=user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
    
    def test_get_matches(self):
        response = self.client.get('/api/matches/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
    
    def test_get_match(self):
        response = self.client.get('/api/matches/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["id"], 1)
    
    def test_post_match(self):
        data = {
            "date": "2020-01-01T12:00:00+00:00",
            "type": "FRIENDSHIP",
            "local_id":  1,
            "visitor_id":  1,
        }
        response = self.client.post('/api/matches/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_put_match(self):
        data = {
            "date": "2020-01-01T12:00:00+00:00",
            "type": "FRIENDSHIP",
            "local_id":  1,
            "visitor_id":  1,
        }
        response = self.client.put('/api/matches/1/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["id"], 1)
    
    def test_delete_match(self):
        response = self.client.delete('/api/matches/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["id"], 1)

    def test_get_players(self):
        response = self.client.get('/api/players/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
    
    def test_get_player(self):
        response = self.client.get('/api/players/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["id"], 1)
    
    def test_post_player(self):
        data = {
            "name": "",
            "photo_id": 1,
            "is_active": False,
            "salary": 128.0,
            "team_id":  1,
            "position_id":  1,
        }
        response = self.client.post('/api/players/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_put_player(self):
        data = {
            "name": "",
            "photo_id": 1,
            "is_active": False,
            "salary": 128.0,
            "team_id":  1,
            "position_id":  1,
        }
        response = self.client.put('/api/players/1/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["id"], 1)
    
    def test_delete_player(self):
        response = self.client.delete('/api/players/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["id"], 1)

    def test_get_player_positions(self):
        response = self.client.get('/api/player_positions/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
    
    def test_get_player_position(self):
        response = self.client.get('/api/player_positions/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["id"], 1)
    
    def test_post_player_position(self):
        data = {
            "name": "",
            "code": "",
            "stats": """{"expected_goals": 8910.0, "dominant_leg": "illum vehicula reprehenderit placeat", "dominant_leg_accuracy": 7850.0}""",
            "details": "{}",
        }
        response = self.client.post('/api/player_positions/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_put_player_position(self):
        data = {
            "name": "",
            "code": "",
            "stats": """{"expected_goals": 2942.0, "dominant_leg": "illum placeat reprehenderit esse", "dominant_leg_accuracy": 713.0}""",
            "details": "{}",
        }
        response = self.client.put('/api/player_positions/1/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["id"], 1)
    
    def test_delete_player_position(self):
        response = self.client.delete('/api/player_positions/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["id"], 1)

    def test_get_scores(self):
        response = self.client.get('/api/scores/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
    
    def test_get_score(self):
        response = self.client.get('/api/scores/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["id"], 1)
    
    def test_post_score(self):
        data = {
            "min": 128,
            "player_id":  1,
            "match_id":  1,
        }
        response = self.client.post('/api/scores/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_put_score(self):
        data = {
            "min": 128,
            "player_id":  1,
            "match_id":  1,
        }
        response = self.client.put('/api/scores/1/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["id"], 1)
    
    def test_delete_score(self):
        response = self.client.delete('/api/scores/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["id"], 1)

    def test_get_teams(self):
        response = self.client.get('/api/teams/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
    
    def test_get_team(self):
        response = self.client.get('/api/teams/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["id"], 1)
    
    def test_post_team(self):
        data = {
            "name": "",
            "logo_id": 1,
            "description": "",
            "market_value": 128.0,
            "rival_id":  1,
        }
        response = self.client.post('/api/teams/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_put_team(self):
        data = {
            "name": "",
            "logo_id": 1,
            "description": "",
            "market_value": 128.0,
            "rival_id":  1,
        }
        response = self.client.put('/api/teams/1/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["id"], 1)
    
    def test_delete_team(self):
        response = self.client.delete('/api/teams/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["id"], 1)

    def test_get_users(self):
        response = self.client.get('/api/users/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
    
    def test_get_user(self):
        response = self.client.get('/api/users/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["id"], 1)
    
    def test_post_user(self):
        data = {
            "username": "email_1@test.com",
            "first_name": "FirstName",
            "last_name": "LastName",
            "email": "email_1@test.com",
            "password": "pbkdf2_sha256$150000$jMOqkdOUpor5$kU/QofjBsopM+CdCnU2+pROhtnxd5CZc7NhUiXNTMc0=",
            "is_active": False,
            "team_ids": [1],
            "profile_image_id": 1,
        }
        response = self.client.post('/api/users/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_put_user(self):
        data = {
            "username": "email_1@test.com",
            "first_name": "FirstName",
            "last_name": "LastName",
            "email": "email_1@test.com",
            "password": "pbkdf2_sha256$150000$jMOqkdOUpor5$kU/QofjBsopM+CdCnU2+pROhtnxd5CZc7NhUiXNTMc0=",
            "is_active": False,
            "team_ids": [1],
            "profile_image_id": 1,
        }
        response = self.client.put('/api/users/1/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["id"], 1)
    
    def test_delete_user(self):
        response = self.client.delete('/api/users/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["id"], 1)