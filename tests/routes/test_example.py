"""
__Seed builder__
  AUTO_GENERATED (Read only)
  Example route tests
"""

import json
from rest_framework import status
from rest_framework.test import APITestCase
from seed.util.test_util import fill_test_database
from dj_rest_auth.models import TokenModel
from app.models import User

class TestExample(APITestCase):
    def setUp(self):
        fill_test_database()
        user = User.objects.all().first()
        token, created = TokenModel.objects.get_or_create(user=user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
    
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