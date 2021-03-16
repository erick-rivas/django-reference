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
        response = self.client.post('/api/matches')
        self.assertIn(response.status_code, [status.HTTP_400_BAD_REQUEST, status.HTTP_201_CREATED])
    
    def test_put_matches(self):
        response = self.client.put('/api/matches/1')
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
        response = self.client.post('/api/players')
        self.assertIn(response.status_code, [status.HTTP_400_BAD_REQUEST, status.HTTP_201_CREATED])
    
    def test_put_players(self):
        response = self.client.put('/api/players/1')
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
        response = self.client.post('/api/player_positions')
        self.assertIn(response.status_code, [status.HTTP_400_BAD_REQUEST, status.HTTP_201_CREATED])
    
    def test_put_player_positions(self):
        response = self.client.put('/api/player_positions/1')
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
        response = self.client.post('/api/scores')
        self.assertIn(response.status_code, [status.HTTP_400_BAD_REQUEST, status.HTTP_201_CREATED])
    
    def test_put_scores(self):
        response = self.client.put('/api/scores/1')
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
        response = self.client.post('/api/teams')
        self.assertIn(response.status_code, [status.HTTP_400_BAD_REQUEST, status.HTTP_201_CREATED])
    
    def test_put_teams(self):
        response = self.client.put('/api/teams/1')
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
        response = self.client.post('/api/users')
        self.assertIn(response.status_code, [status.HTTP_400_BAD_REQUEST, status.HTTP_201_CREATED])
    
    def test_put_users(self):
        response = self.client.put('/api/users/1')
        res = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(res["id"], 1)
    
    def test_delete_users(self):
        response = self.client.delete('/api/users/1')
        res = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(res["id"], 1)