"""
__Seed builder__v0.2.0
  AUTO_GENERATED (Read only)
  Modify via builder
"""

import json

from graphene_django.utils.testing import GraphQLTestCase

from seed.tests.util import fill_test_database

class TestGraphql(GraphQLTestCase):
    GRAPHQL_URL = "/graphql"

    def setUp(self):
        fill_test_database()
    
    def test_query_matches(self):
        response = self.query(
            '''
            {
                matches(query: "id=1", orderBy: "id", start: 0, end: 1){ id }
            }
            ''')
        res = json.loads(response.content)["data"]
        self.assertResponseNoErrors(response)
        self.assertEqual(res["matches"][0]["id"], 1)
    
    def test_query_match(self):
        response = self.query(
            '''
            {
                match(id: 1){ id }
            }
            ''')
        res = json.loads(response.content)["data"]
        self.assertResponseNoErrors(response)
        self.assertEqual(res["match"]["id"], 1)
    
    def test_set_match(self):
        response = self.query(
            '''
            mutation {
                setMatch(id:1) {
                    match { id }
                }
            }
            '''
        )
        res = json.loads(response.content)["data"]
        self.assertResponseNoErrors(response)
        self.assertEqual(res["setMatch"]["match"]["id"], 1)
    
    def test_delete_match(self):
        response = self.query(
            '''
            mutation {
                deleteMatch(id:1) { id }
            }
            '''
        )
        res = json.loads(response.content)["data"]
        self.assertResponseNoErrors(response)
        self.assertEqual(res["deleteMatch"]["id"], 1)

    def test_query_players(self):
        response = self.query(
            '''
            {
                players(query: "id=1", orderBy: "id", start: 0, end: 1){ id }
            }
            ''')
        res = json.loads(response.content)["data"]
        self.assertResponseNoErrors(response)
        self.assertEqual(res["players"][0]["id"], 1)
    
    def test_query_player(self):
        response = self.query(
            '''
            {
                player(id: 1){ id }
            }
            ''')
        res = json.loads(response.content)["data"]
        self.assertResponseNoErrors(response)
        self.assertEqual(res["player"]["id"], 1)
    
    def test_set_player(self):
        response = self.query(
            '''
            mutation {
                setPlayer(id:1) {
                    player { id }
                }
            }
            '''
        )
        res = json.loads(response.content)["data"]
        self.assertResponseNoErrors(response)
        self.assertEqual(res["setPlayer"]["player"]["id"], 1)
    
    def test_delete_player(self):
        response = self.query(
            '''
            mutation {
                deletePlayer(id:1) { id }
            }
            '''
        )
        res = json.loads(response.content)["data"]
        self.assertResponseNoErrors(response)
        self.assertEqual(res["deletePlayer"]["id"], 1)

    def test_query_player_positions(self):
        response = self.query(
            '''
            {
                playerPositions(query: "id=1", orderBy: "id", start: 0, end: 1){ id }
            }
            ''')
        res = json.loads(response.content)["data"]
        self.assertResponseNoErrors(response)
        self.assertEqual(res["playerPositions"][0]["id"], 1)
    
    def test_query_player_position(self):
        response = self.query(
            '''
            {
                playerPosition(id: 1){ id }
            }
            ''')
        res = json.loads(response.content)["data"]
        self.assertResponseNoErrors(response)
        self.assertEqual(res["playerPosition"]["id"], 1)
    
    def test_set_player_position(self):
        response = self.query(
            '''
            mutation {
                setPlayerPosition(id:1) {
                    playerPosition { id }
                }
            }
            '''
        )
        res = json.loads(response.content)["data"]
        self.assertResponseNoErrors(response)
        self.assertEqual(res["setPlayerPosition"]["playerPosition"]["id"], 1)
    
    def test_delete_player_position(self):
        response = self.query(
            '''
            mutation {
                deletePlayerPosition(id:1) { id }
            }
            '''
        )
        res = json.loads(response.content)["data"]
        self.assertResponseNoErrors(response)
        self.assertEqual(res["deletePlayerPosition"]["id"], 1)

    def test_query_scores(self):
        response = self.query(
            '''
            {
                scores(query: "id=1", orderBy: "id", start: 0, end: 1){ id }
            }
            ''')
        res = json.loads(response.content)["data"]
        self.assertResponseNoErrors(response)
        self.assertEqual(res["scores"][0]["id"], 1)
    
    def test_query_score(self):
        response = self.query(
            '''
            {
                score(id: 1){ id }
            }
            ''')
        res = json.loads(response.content)["data"]
        self.assertResponseNoErrors(response)
        self.assertEqual(res["score"]["id"], 1)
    
    def test_set_score(self):
        response = self.query(
            '''
            mutation {
                setScore(id:1) {
                    score { id }
                }
            }
            '''
        )
        res = json.loads(response.content)["data"]
        self.assertResponseNoErrors(response)
        self.assertEqual(res["setScore"]["score"]["id"], 1)
    
    def test_delete_score(self):
        response = self.query(
            '''
            mutation {
                deleteScore(id:1) { id }
            }
            '''
        )
        res = json.loads(response.content)["data"]
        self.assertResponseNoErrors(response)
        self.assertEqual(res["deleteScore"]["id"], 1)

    def test_query_teams(self):
        response = self.query(
            '''
            {
                teams(query: "id=1", orderBy: "id", start: 0, end: 1){ id }
            }
            ''')
        res = json.loads(response.content)["data"]
        self.assertResponseNoErrors(response)
        self.assertEqual(res["teams"][0]["id"], 1)
    
    def test_query_team(self):
        response = self.query(
            '''
            {
                team(id: 1){ id }
            }
            ''')
        res = json.loads(response.content)["data"]
        self.assertResponseNoErrors(response)
        self.assertEqual(res["team"]["id"], 1)
    
    def test_set_team(self):
        response = self.query(
            '''
            mutation {
                setTeam(id:1) {
                    team { id }
                }
            }
            '''
        )
        res = json.loads(response.content)["data"]
        self.assertResponseNoErrors(response)
        self.assertEqual(res["setTeam"]["team"]["id"], 1)
    
    def test_delete_team(self):
        response = self.query(
            '''
            mutation {
                deleteTeam(id:1) { id }
            }
            '''
        )
        res = json.loads(response.content)["data"]
        self.assertResponseNoErrors(response)
        self.assertEqual(res["deleteTeam"]["id"], 1)

    def test_query_users(self):
        response = self.query(
            '''
            {
                users(query: "id=1", orderBy: "id", start: 0, end: 1){ id }
            }
            ''')
        res = json.loads(response.content)["data"]
        self.assertResponseNoErrors(response)
        self.assertEqual(res["users"][0]["id"], 1)
    
    def test_query_user(self):
        response = self.query(
            '''
            {
                user(id: 1){ id }
            }
            ''')
        res = json.loads(response.content)["data"]
        self.assertResponseNoErrors(response)
        self.assertEqual(res["user"]["id"], 1)
    
    def test_set_user(self):
        response = self.query(
            '''
            mutation {
                setUser(id:1) {
                    user { id }
                }
            }
            '''
        )
        res = json.loads(response.content)["data"]
        self.assertResponseNoErrors(response)
        self.assertEqual(res["setUser"]["user"]["id"], 1)
    
    def test_delete_user(self):
        response = self.query(
            '''
            mutation {
                deleteUser(id:1) { id }
            }
            '''
        )
        res = json.loads(response.content)["data"]
        self.assertResponseNoErrors(response)
        self.assertEqual(res["deleteUser"]["id"], 1)