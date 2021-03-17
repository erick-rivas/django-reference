"""
__Seed builder__v0.2.0
  AUTO_GENERATED (Read only)
  Modify via builder
"""

import json

from rest_framework import status
from rest_framework.test import APITestCase

from seed.tests.util_test import fill_test_database

class TestRest(APITestCase):
    def setUp(self):
        fill_test_database()
    
    def test_get_matches(self):
        response = self.client.get('/api/matches')
        res = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
    
    def test_get_match(self):
        response = self.client.get('/api/matches/1')
        res = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(res["id"], 1)
    
    def test_post_matches(self):
        data = {
            "date": "2020-01-01T12:00:00+00:00",
            "type": "FRIENDSHIP",
            "local_id":  1,
            "visitor_id":  1,
        }
        response = self.client.post('/api/matches', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_put_matches(self):
        data = {
            "date": "2020-01-01T12:00:00+00:00",
            "type": "FRIENDSHIP",
            "local_id":  1,
            "visitor_id":  1,
        }
        response = self.client.put('/api/matches/1', data)
        res = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(res["id"], 1)
    
    def test_delete_matches(self):
        response = self.client.delete('/api/matches/1')
        res = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(res["id"], 1)

    def test_get_players(self):
        response = self.client.get('/api/players')
        res = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
    
    def test_get_player(self):
        response = self.client.get('/api/players/1')
        res = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(res["id"], 1)
    
    def test_post_players(self):
        data = {
            "name": "",
            "photo_id": 1,
            "is_active": False,
            "team_id":  1,
            "position_id":  1,
        }
        response = self.client.post('/api/players', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_put_players(self):
        data = {
            "name": "",
            "photo_id": 1,
            "is_active": False,
            "team_id":  1,
            "position_id":  1,
        }
        response = self.client.put('/api/players/1', data)
        res = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(res["id"], 1)
    
    def test_delete_players(self):
        response = self.client.delete('/api/players/1')
        res = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(res["id"], 1)

    def test_get_player_positions(self):
        response = self.client.get('/api/player_positions')
        res = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
    
    def test_get_player_position(self):
        response = self.client.get('/api/player_positions/1')
        res = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(res["id"], 1)
    
    def test_post_player_positions(self):
        data = {
            "name": "",
        }
        response = self.client.post('/api/player_positions', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_put_player_positions(self):
        data = {
            "name": "",
        }
        response = self.client.put('/api/player_positions/1', data)
        res = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(res["id"], 1)
    
    def test_delete_player_positions(self):
        response = self.client.delete('/api/player_positions/1')
        res = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(res["id"], 1)

    def test_get_scores(self):
        response = self.client.get('/api/scores')
        res = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
    
    def test_get_score(self):
        response = self.client.get('/api/scores/1')
        res = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(res["id"], 1)
    
    def test_post_scores(self):
        data = {
            "min": 128,
            "player_id":  1,
            "match_id":  1,
        }
        response = self.client.post('/api/scores', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_put_scores(self):
        data = {
            "min": 128,
            "player_id":  1,
            "match_id":  1,
        }
        response = self.client.put('/api/scores/1', data)
        res = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(res["id"], 1)
    
    def test_delete_scores(self):
        response = self.client.delete('/api/scores/1')
        res = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(res["id"], 1)

    def test_get_teams(self):
        response = self.client.get('/api/teams')
        res = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
    
    def test_get_team(self):
        response = self.client.get('/api/teams/1')
        res = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(res["id"], 1)
    
    def test_post_teams(self):
        data = {
            "name": "",
            "logo_id": 1,
            "description": "",
            "market_value": 128.0,
            "rival_id":  1,
        }
        response = self.client.post('/api/teams', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_put_teams(self):
        data = {
            "name": "",
            "logo_id": 1,
            "description": "",
            "market_value": 128.0,
            "rival_id":  1,
        }
        response = self.client.put('/api/teams/1', data)
        res = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(res["id"], 1)
    
    def test_delete_teams(self):
        response = self.client.delete('/api/teams/1')
        res = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(res["id"], 1)

    def test_get_users(self):
        response = self.client.get('/api/users')
        res = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
    
    def test_get_user(self):
        response = self.client.get('/api/users/1')
        res = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(res["id"], 1)
    
    def test_post_users(self):
        data = {
            "username": "email_1@test.com",
            "first_name": "FirstName",
            "last_name": "LastName",
            "email": "email_1@test.com",
            "password": "pbkdf2_sha256$150000$jMOqkdOUpor5$kU/QofjBsopM+CdCnU2+pROhtnxd5CZc7NhUiXNTMc0=",
            "is_active": False,
            "team_ids": [1],
        }
        response = self.client.post('/api/users', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_put_users(self):
        data = {
            "username": "email_1@test.com",
            "first_name": "FirstName",
            "last_name": "LastName",
            "email": "email_1@test.com",
            "password": "pbkdf2_sha256$150000$jMOqkdOUpor5$kU/QofjBsopM+CdCnU2+pROhtnxd5CZc7NhUiXNTMc0=",
            "is_active": False,
            "team_ids": [1],
        }
        response = self.client.put('/api/users/1', data)
        res = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(res["id"], 1)
    
    def test_delete_users(self):
        response = self.client.delete('/api/users/1')
        res = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(res["id"], 1)