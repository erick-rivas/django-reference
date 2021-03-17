"""
__Seed builder__v0.2.0
  AUTO_GENERATED (Read only)
  Modify via builder
"""

import json

from graphene_django.utils.testing import GraphQLTestCase

from seed.tests.util_test import fill_test_database

class TestGraphql(GraphQLTestCase):
    GRAPHQL_URL = "/graphql"

    def setUp(self):
        fill_test_database()
    
    def test_query_matches(self):
        response_01 = self.query(
            '''
            {
                matches(query: "id=1", orderBy: "id", start: 0, end: 1){
                    id
                    date
                    type
                    local {
                      id
                    }
                    visitor {
                      id
                    }
                }
            }
            ''')
        res_01 = json.loads(response_01.content)["data"]
        self.assertResponseNoErrors(response_01)
        with self.subTest():
            self.assertEqual(res_01["matches"][0]["id"], 1)

        response_02 = self.query(
            '''
            {
                matches{ id }
            }
            ''')
        res_02 = json.loads(response_02.content)["data"]
        self.assertResponseNoErrors(response_02)
        with self.subTest():
            self.assertEqual(res_02["matches"][0]["id"], 1)

        response_03 = self.query(
            '''
            {
                matchCount(query: "id=1"){ count }
            }
            ''')
        res_03 = json.loads(response_03.content)["data"]
        self.assertResponseNoErrors(response_03)
        with self.subTest():
            self.assertEqual(res_03["matchCount"]["count"], 1)

        response_04 = self.query(
            '''
            {
                matchCount { count }
            }
            ''')
        res_04 = json.loads(response_04.content)["data"]
        self.assertResponseNoErrors(response_04)
        with self.subTest():
            self.assertEqual(res_04["matchCount"]["count"], 1)

    def test_query_match(self):
        response = self.query(
            '''
            {
                match(id: 1){
                    id
                    date
                    type
                    local {
                      id
                    }
                    visitor {
                      id
                    }
                }
            }
            ''')
        res = json.loads(response.content)["data"]
        self.assertResponseNoErrors(response)
        self.assertEqual(res["match"]["id"], 1)
    
    def test_save_match(self):
        response = self.query(
            '''
            mutation {
                saveMatch(
                    date: "2020-01-01T12:00:00+00:00",
                    type: "FRIENDSHIP",
                    local:  1,
                    visitor:  1,
                ) {
                    match {
                        id
                        date
                        type
                        local {
                          id
                        }
                        visitor {
                          id
                        }
                    }
                }
            }
            '''
        )
        res = json.loads(response.content)["data"]
        self.assertResponseNoErrors(response)
        self.assertEqual(res["saveMatch"]["match"]["id"], 2)
    
    def test_set_match(self):
        response = self.query(
            '''
            mutation {
                setMatch(id:1
                    date: "2020-01-01T12:00:00+00:00",
                    type: "FRIENDSHIP",
                    local:  1,
                    visitor:  1,

                ) {
                    match {
                        id
                        date
                        type
                        local {
                          id
                        }
                        visitor {
                          id
                        }
                    }
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
        response_01 = self.query(
            '''
            {
                players(query: "id=1", orderBy: "id", start: 0, end: 1){
                    id
                    name
                    isActive
                    photo {
                      id
                    }
                    team {
                      id
                    }
                    position {
                      id
                    }
                }
            }
            ''')
        res_01 = json.loads(response_01.content)["data"]
        self.assertResponseNoErrors(response_01)
        with self.subTest():
            self.assertEqual(res_01["players"][0]["id"], 1)

        response_02 = self.query(
            '''
            {
                players{ id }
            }
            ''')
        res_02 = json.loads(response_02.content)["data"]
        self.assertResponseNoErrors(response_02)
        with self.subTest():
            self.assertEqual(res_02["players"][0]["id"], 1)

        response_03 = self.query(
            '''
            {
                playerCount(query: "id=1"){ count }
            }
            ''')
        res_03 = json.loads(response_03.content)["data"]
        self.assertResponseNoErrors(response_03)
        with self.subTest():
            self.assertEqual(res_03["playerCount"]["count"], 1)

        response_04 = self.query(
            '''
            {
                playerCount { count }
            }
            ''')
        res_04 = json.loads(response_04.content)["data"]
        self.assertResponseNoErrors(response_04)
        with self.subTest():
            self.assertEqual(res_04["playerCount"]["count"], 1)

    def test_query_player(self):
        response = self.query(
            '''
            {
                player(id: 1){
                    id
                    name
                    isActive
                    photo {
                      id
                    }
                    team {
                      id
                    }
                    position {
                      id
                    }
                }
            }
            ''')
        res = json.loads(response.content)["data"]
        self.assertResponseNoErrors(response)
        self.assertEqual(res["player"]["id"], 1)
    
    def test_save_player(self):
        response = self.query(
            '''
            mutation {
                savePlayer(
                    name: "",
                    photo: 1,
                    isActive: false,
                    team:  1,
                    position:  1,
                ) {
                    player {
                        id
                        name
                        isActive
                        photo {
                          id
                        }
                        team {
                          id
                        }
                        position {
                          id
                        }
                    }
                }
            }
            '''
        )
        res = json.loads(response.content)["data"]
        self.assertResponseNoErrors(response)
        self.assertEqual(res["savePlayer"]["player"]["id"], 2)
    
    def test_set_player(self):
        response = self.query(
            '''
            mutation {
                setPlayer(id:1
                    name: "",
                    photo: 1,
                    isActive: false,
                    team:  1,
                    position:  1,

                ) {
                    player {
                        id
                        name
                        isActive
                        photo {
                          id
                        }
                        team {
                          id
                        }
                        position {
                          id
                        }
                    }
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
        response_01 = self.query(
            '''
            {
                playerPositions(query: "id=1", orderBy: "id", start: 0, end: 1){
                    id
                    name
                }
            }
            ''')
        res_01 = json.loads(response_01.content)["data"]
        self.assertResponseNoErrors(response_01)
        with self.subTest():
            self.assertEqual(res_01["playerPositions"][0]["id"], 1)

        response_02 = self.query(
            '''
            {
                playerPositions{ id }
            }
            ''')
        res_02 = json.loads(response_02.content)["data"]
        self.assertResponseNoErrors(response_02)
        with self.subTest():
            self.assertEqual(res_02["playerPositions"][0]["id"], 1)

        response_03 = self.query(
            '''
            {
                playerPositionCount(query: "id=1"){ count }
            }
            ''')
        res_03 = json.loads(response_03.content)["data"]
        self.assertResponseNoErrors(response_03)
        with self.subTest():
            self.assertEqual(res_03["playerPositionCount"]["count"], 1)

        response_04 = self.query(
            '''
            {
                playerPositionCount { count }
            }
            ''')
        res_04 = json.loads(response_04.content)["data"]
        self.assertResponseNoErrors(response_04)
        with self.subTest():
            self.assertEqual(res_04["playerPositionCount"]["count"], 1)

    def test_query_player_position(self):
        response = self.query(
            '''
            {
                playerPosition(id: 1){
                    id
                    name
                }
            }
            ''')
        res = json.loads(response.content)["data"]
        self.assertResponseNoErrors(response)
        self.assertEqual(res["playerPosition"]["id"], 1)
    
    def test_save_player_position(self):
        response = self.query(
            '''
            mutation {
                savePlayerPosition(
                    name: "",
                ) {
                    playerPosition {
                        id
                        name
                    }
                }
            }
            '''
        )
        res = json.loads(response.content)["data"]
        self.assertResponseNoErrors(response)
        self.assertEqual(res["savePlayerPosition"]["playerPosition"]["id"], 2)
    
    def test_set_player_position(self):
        response = self.query(
            '''
            mutation {
                setPlayerPosition(id:1
                    name: "",

                ) {
                    playerPosition {
                        id
                        name
                    }
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
        response_01 = self.query(
            '''
            {
                scores(query: "id=1", orderBy: "id", start: 0, end: 1){
                    id
                    min
                    player {
                      id
                    }
                    match {
                      id
                    }
                }
            }
            ''')
        res_01 = json.loads(response_01.content)["data"]
        self.assertResponseNoErrors(response_01)
        with self.subTest():
            self.assertEqual(res_01["scores"][0]["id"], 1)

        response_02 = self.query(
            '''
            {
                scores{ id }
            }
            ''')
        res_02 = json.loads(response_02.content)["data"]
        self.assertResponseNoErrors(response_02)
        with self.subTest():
            self.assertEqual(res_02["scores"][0]["id"], 1)

        response_03 = self.query(
            '''
            {
                scoreCount(query: "id=1"){ count }
            }
            ''')
        res_03 = json.loads(response_03.content)["data"]
        self.assertResponseNoErrors(response_03)
        with self.subTest():
            self.assertEqual(res_03["scoreCount"]["count"], 1)

        response_04 = self.query(
            '''
            {
                scoreCount { count }
            }
            ''')
        res_04 = json.loads(response_04.content)["data"]
        self.assertResponseNoErrors(response_04)
        with self.subTest():
            self.assertEqual(res_04["scoreCount"]["count"], 1)

    def test_query_score(self):
        response = self.query(
            '''
            {
                score(id: 1){
                    id
                    min
                    player {
                      id
                    }
                    match {
                      id
                    }
                }
            }
            ''')
        res = json.loads(response.content)["data"]
        self.assertResponseNoErrors(response)
        self.assertEqual(res["score"]["id"], 1)
    
    def test_save_score(self):
        response = self.query(
            '''
            mutation {
                saveScore(
                    min: 128,
                    player:  1,
                    match:  1,
                ) {
                    score {
                        id
                        min
                        player {
                          id
                        }
                        match {
                          id
                        }
                    }
                }
            }
            '''
        )
        res = json.loads(response.content)["data"]
        self.assertResponseNoErrors(response)
        self.assertEqual(res["saveScore"]["score"]["id"], 2)
    
    def test_set_score(self):
        response = self.query(
            '''
            mutation {
                setScore(id:1
                    min: 128,
                    player:  1,
                    match:  1,

                ) {
                    score {
                        id
                        min
                        player {
                          id
                        }
                        match {
                          id
                        }
                    }
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
        response_01 = self.query(
            '''
            {
                teams(query: "id=1", orderBy: "id", start: 0, end: 1){
                    id
                    name
                    description
                    marketValue
                    logo {
                      id
                    }
                    rival {
                      id
                    }
                }
            }
            ''')
        res_01 = json.loads(response_01.content)["data"]
        self.assertResponseNoErrors(response_01)
        with self.subTest():
            self.assertEqual(res_01["teams"][0]["id"], 1)

        response_02 = self.query(
            '''
            {
                teams{ id }
            }
            ''')
        res_02 = json.loads(response_02.content)["data"]
        self.assertResponseNoErrors(response_02)
        with self.subTest():
            self.assertEqual(res_02["teams"][0]["id"], 1)

        response_03 = self.query(
            '''
            {
                teamCount(query: "id=1"){ count }
            }
            ''')
        res_03 = json.loads(response_03.content)["data"]
        self.assertResponseNoErrors(response_03)
        with self.subTest():
            self.assertEqual(res_03["teamCount"]["count"], 1)

        response_04 = self.query(
            '''
            {
                teamCount { count }
            }
            ''')
        res_04 = json.loads(response_04.content)["data"]
        self.assertResponseNoErrors(response_04)
        with self.subTest():
            self.assertEqual(res_04["teamCount"]["count"], 1)

    def test_query_team(self):
        response = self.query(
            '''
            {
                team(id: 1){
                    id
                    name
                    description
                    marketValue
                    logo {
                      id
                    }
                    rival {
                      id
                    }
                }
            }
            ''')
        res = json.loads(response.content)["data"]
        self.assertResponseNoErrors(response)
        self.assertEqual(res["team"]["id"], 1)
    
    def test_save_team(self):
        response = self.query(
            '''
            mutation {
                saveTeam(
                    name: "",
                    logo: 1,
                    description: "",
                    marketValue: 128.0,
                    rival:  1,
                ) {
                    team {
                        id
                        name
                        description
                        marketValue
                        logo {
                          id
                        }
                        rival {
                          id
                        }
                    }
                }
            }
            '''
        )
        res = json.loads(response.content)["data"]
        self.assertResponseNoErrors(response)
        self.assertEqual(res["saveTeam"]["team"]["id"], 2)
    
    def test_set_team(self):
        response = self.query(
            '''
            mutation {
                setTeam(id:1
                    name: "",
                    logo: 1,
                    description: "",
                    marketValue: 128.0,
                    rival:  1,

                ) {
                    team {
                        id
                        name
                        description
                        marketValue
                        logo {
                          id
                        }
                        rival {
                          id
                        }
                    }
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
        response_01 = self.query(
            '''
            {
                users(query: "id=1", orderBy: "id", start: 0, end: 1){
                    id
                    username
                    firstName
                    lastName
                    email
                    isActive
                    teams {
                      id
                    }
                }
            }
            ''')
        res_01 = json.loads(response_01.content)["data"]
        self.assertResponseNoErrors(response_01)
        with self.subTest():
            self.assertEqual(res_01["users"][0]["id"], 1)

        response_02 = self.query(
            '''
            {
                users{ id }
            }
            ''')
        res_02 = json.loads(response_02.content)["data"]
        self.assertResponseNoErrors(response_02)
        with self.subTest():
            self.assertEqual(res_02["users"][0]["id"], 1)

        response_03 = self.query(
            '''
            {
                userCount(query: "id=1"){ count }
            }
            ''')
        res_03 = json.loads(response_03.content)["data"]
        self.assertResponseNoErrors(response_03)
        with self.subTest():
            self.assertEqual(res_03["userCount"]["count"], 1)

        response_04 = self.query(
            '''
            {
                userCount { count }
            }
            ''')
        res_04 = json.loads(response_04.content)["data"]
        self.assertResponseNoErrors(response_04)
        with self.subTest():
            self.assertEqual(res_04["userCount"]["count"], 1)

    def test_query_user(self):
        response = self.query(
            '''
            {
                user(id: 1){
                    id
                    username
                    firstName
                    lastName
                    email
                    isActive
                    teams {
                      id
                    }
                }
            }
            ''')
        res = json.loads(response.content)["data"]
        self.assertResponseNoErrors(response)
        self.assertEqual(res["user"]["id"], 1)
    
    def test_save_user(self):
        response = self.query(
            '''
            mutation {
                saveUser(
                    username: "email@test.com",
                    firstName: "FirstName",
                    lastName: "LastName",
                    email: "email@test.com",
                    password: "pbkdf2_sha256$150000$jMOqkdOUpor5$kU/QofjBsopM+CdCnU2+pROhtnxd5CZc7NhUiXNTMc0=",
                    isActive: true,
                    teams: [1],
                ) {
                    user {
                        id
                        username
                        firstName
                        lastName
                        email
                        isActive
                        teams {
                          id
                        }
                    }
                }
            }
            '''
        )
        res = json.loads(response.content)["data"]
        self.assertResponseNoErrors(response)
        self.assertEqual(res["saveUser"]["user"]["id"], 2)
    
    def test_set_user(self):
        response = self.query(
            '''
            mutation {
                setUser(id:1
                    username: "email_1@test.com",
                    firstName: "FirstName",
                    lastName: "LastName",
                    email: "email_1@test.com",
                    password: "pbkdf2_sha256$150000$jMOqkdOUpor5$kU/QofjBsopM+CdCnU2+pROhtnxd5CZc7NhUiXNTMc0=",
                    isActive: true,
                    teams: [1],

                ) {
                    user {
                        id
                        username
                        firstName
                        lastName
                        email
                        isActive
                        teams {
                          id
                        }
                    }
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