"""
__Seed builder__
  AUTO_GENERATED (Read only)
  Modify via builder
"""

import json
from graphene_django.utils.testing import GraphQLTestCase
from seed.util.test_util import fill_test_database
from dj_rest_auth.models import TokenModel
from app.models import User

class TestGraphql(GraphQLTestCase):
    GRAPHQL_URL = "/graphql"

    def setUp(self):
        fill_test_database()
        user = User.objects.all().first()
        token, created = TokenModel.objects.get_or_create(user=user)
        self.headers = {"authorization": 'Token ' + token.key}
    
    def test_query_matches(self):
        response_01 = self.query(
            '''
            {
                matches(query: "id=1", orderBy: "id", limit: 1){
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
            ''', headers=self.headers)
        res_01 = json.loads(response_01.content)["data"]
        self.assertResponseNoErrors(response_01)
        with self.subTest():
            self.assertEqual(res_01["matches"][0]["id"], 1)

        response_02 = self.query(
            '''
            {
                matches{ id }
            }
            ''', headers=self.headers)
        res_02 = json.loads(response_02.content)["data"]
        self.assertResponseNoErrors(response_02)
        with self.subTest():
            self.assertEqual(res_02["matches"][0]["id"], 1)

        response_03 = self.query(
            '''
            {
                matchPagination(pageNum: 1, pageSize: 1){
                    pageNum
                    pageSize
                    totalPages
                    totalCount
                    matches { id }
                }
            }
            ''', headers=self.headers)
        res_03 = json.loads(response_03.content)["data"]
        self.assertResponseNoErrors(response_03)
        with self.subTest():
            self.assertEqual(res_03["matchPagination"]["totalPages"], 1)
            self.assertEqual(res_03["matchPagination"]["totalCount"], 1)
            self.assertEqual(res_03["matchPagination"]["matches"][0]["id"], 1)

        response_04 = self.query(
            '''
            {
                matchCount(query: "id=1"){ count }
            }
            ''', headers=self.headers)
        res_04 = json.loads(response_04.content)["data"]
        self.assertResponseNoErrors(response_04)
        with self.subTest():
            self.assertEqual(res_04["matchCount"]["count"], 1)

        response_05 = self.query(
            '''
            {
                matchCount { count }
            }
            ''', headers=self.headers)
        res_05 = json.loads(response_05.content)["data"]
        self.assertResponseNoErrors(response_05)
        with self.subTest():
            self.assertEqual(res_05["matchCount"]["count"], 1)

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
            ''', headers=self.headers)
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
            ''', headers=self.headers)
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
            ''', headers=self.headers)
        res = json.loads(response.content)["data"]
        self.assertResponseNoErrors(response)
        self.assertEqual(res["setMatch"]["match"]["id"], 1)
    
    def test_delete_match(self):
        response = self.query(
            '''
            mutation {
                deleteMatch(id:1) { id }
            }
            ''', headers=self.headers)
        res = json.loads(response.content)["data"]
        self.assertResponseNoErrors(response)
        self.assertEqual(res["deleteMatch"]["id"], 1)

    def test_query_players(self):
        response_01 = self.query(
            '''
            {
                players(query: "id=1", orderBy: "id", limit: 1){
                    id
                    name
                    isActive
                    salary
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
            ''', headers=self.headers)
        res_01 = json.loads(response_01.content)["data"]
        self.assertResponseNoErrors(response_01)
        with self.subTest():
            self.assertEqual(res_01["players"][0]["id"], 1)

        response_02 = self.query(
            '''
            {
                players{ id }
            }
            ''', headers=self.headers)
        res_02 = json.loads(response_02.content)["data"]
        self.assertResponseNoErrors(response_02)
        with self.subTest():
            self.assertEqual(res_02["players"][0]["id"], 1)

        response_03 = self.query(
            '''
            {
                playerPagination(pageNum: 1, pageSize: 1){
                    pageNum
                    pageSize
                    totalPages
                    totalCount
                    players { id }
                }
            }
            ''', headers=self.headers)
        res_03 = json.loads(response_03.content)["data"]
        self.assertResponseNoErrors(response_03)
        with self.subTest():
            self.assertEqual(res_03["playerPagination"]["totalPages"], 1)
            self.assertEqual(res_03["playerPagination"]["totalCount"], 1)
            self.assertEqual(res_03["playerPagination"]["players"][0]["id"], 1)

        response_04 = self.query(
            '''
            {
                playerCount(query: "id=1"){ count }
            }
            ''', headers=self.headers)
        res_04 = json.loads(response_04.content)["data"]
        self.assertResponseNoErrors(response_04)
        with self.subTest():
            self.assertEqual(res_04["playerCount"]["count"], 1)

        response_05 = self.query(
            '''
            {
                playerCount { count }
            }
            ''', headers=self.headers)
        res_05 = json.loads(response_05.content)["data"]
        self.assertResponseNoErrors(response_05)
        with self.subTest():
            self.assertEqual(res_05["playerCount"]["count"], 1)

    def test_query_player(self):
        response = self.query(
            '''
            {
                player(id: 1){
                    id
                    name
                    isActive
                    salary
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
            ''', headers=self.headers)
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
                    salary: 128.0,
                    team:  1,
                    position:  1,
                ) {
                    player {
                        id
                        name
                        isActive
                        salary
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
            ''', headers=self.headers)
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
                    salary: 128.0,
                    team:  1,
                    position:  1,

                ) {
                    player {
                        id
                        name
                        isActive
                        salary
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
            ''', headers=self.headers)
        res = json.loads(response.content)["data"]
        self.assertResponseNoErrors(response)
        self.assertEqual(res["setPlayer"]["player"]["id"], 1)
    
    def test_delete_player(self):
        response = self.query(
            '''
            mutation {
                deletePlayer(id:1) { id }
            }
            ''', headers=self.headers)
        res = json.loads(response.content)["data"]
        self.assertResponseNoErrors(response)
        self.assertEqual(res["deletePlayer"]["id"], 1)

    def test_query_player_positions(self):
        response_01 = self.query(
            '''
            {
                playerPositions(query: "id=1", orderBy: "id", limit: 1){
                    id
                    name
                    code
                    stats
                    details
                }
            }
            ''', headers=self.headers)
        res_01 = json.loads(response_01.content)["data"]
        self.assertResponseNoErrors(response_01)
        with self.subTest():
            self.assertEqual(res_01["playerPositions"][0]["id"], 1)

        response_02 = self.query(
            '''
            {
                playerPositions{ id }
            }
            ''', headers=self.headers)
        res_02 = json.loads(response_02.content)["data"]
        self.assertResponseNoErrors(response_02)
        with self.subTest():
            self.assertEqual(res_02["playerPositions"][0]["id"], 1)

        response_03 = self.query(
            '''
            {
                playerPositionPagination(pageNum: 1, pageSize: 1){
                    pageNum
                    pageSize
                    totalPages
                    totalCount
                    playerPositions { id }
                }
            }
            ''', headers=self.headers)
        res_03 = json.loads(response_03.content)["data"]
        self.assertResponseNoErrors(response_03)
        with self.subTest():
            self.assertEqual(res_03["playerPositionPagination"]["totalPages"], 1)
            self.assertEqual(res_03["playerPositionPagination"]["totalCount"], 1)
            self.assertEqual(res_03["playerPositionPagination"]["playerPositions"][0]["id"], 1)

        response_04 = self.query(
            '''
            {
                playerPositionCount(query: "id=1"){ count }
            }
            ''', headers=self.headers)
        res_04 = json.loads(response_04.content)["data"]
        self.assertResponseNoErrors(response_04)
        with self.subTest():
            self.assertEqual(res_04["playerPositionCount"]["count"], 1)

        response_05 = self.query(
            '''
            {
                playerPositionCount { count }
            }
            ''', headers=self.headers)
        res_05 = json.loads(response_05.content)["data"]
        self.assertResponseNoErrors(response_05)
        with self.subTest():
            self.assertEqual(res_05["playerPositionCount"]["count"], 1)

    def test_query_player_position(self):
        response = self.query(
            '''
            {
                playerPosition(id: 1){
                    id
                    name
                    code
                    stats
                    details
                }
            }
            ''', headers=self.headers)
        res = json.loads(response.content)["data"]
        self.assertResponseNoErrors(response)
        self.assertEqual(res["playerPosition"]["id"], 1)
    
    def test_save_player_position(self):
        response = self.query(
            '''
            mutation {
                savePlayerPosition(
                    name: "",
                    code: "",
                    stats: """{"expected_goals": 4143.0, "dominant_leg": "exercitationem arcu congue. repellendus arcu"}""",
                    details: "{}",
                ) {
                    playerPosition {
                        id
                        name
                        code
                        stats
                        details
                    }
                }
            }
            ''', headers=self.headers)
        res = json.loads(response.content)["data"]
        self.assertResponseNoErrors(response)
        self.assertEqual(res["savePlayerPosition"]["playerPosition"]["id"], 2)
    
    def test_set_player_position(self):
        response = self.query(
            '''
            mutation {
                setPlayerPosition(id:1
                    name: "",
                    code: "",
                    stats: """{"expected_goals": 2737.0, "dominant_leg": ""}""",
                    details: "{}",

                ) {
                    playerPosition {
                        id
                        name
                        code
                        stats
                        details
                    }
                }
            }
            ''', headers=self.headers)
        res = json.loads(response.content)["data"]
        self.assertResponseNoErrors(response)
        self.assertEqual(res["setPlayerPosition"]["playerPosition"]["id"], 1)
    
    def test_delete_player_position(self):
        response = self.query(
            '''
            mutation {
                deletePlayerPosition(id:1) { id }
            }
            ''', headers=self.headers)
        res = json.loads(response.content)["data"]
        self.assertResponseNoErrors(response)
        self.assertEqual(res["deletePlayerPosition"]["id"], 1)

    def test_query_scores(self):
        response_01 = self.query(
            '''
            {
                scores(query: "id=1", orderBy: "id", limit: 1){
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
            ''', headers=self.headers)
        res_01 = json.loads(response_01.content)["data"]
        self.assertResponseNoErrors(response_01)
        with self.subTest():
            self.assertEqual(res_01["scores"][0]["id"], 1)

        response_02 = self.query(
            '''
            {
                scores{ id }
            }
            ''', headers=self.headers)
        res_02 = json.loads(response_02.content)["data"]
        self.assertResponseNoErrors(response_02)
        with self.subTest():
            self.assertEqual(res_02["scores"][0]["id"], 1)

        response_03 = self.query(
            '''
            {
                scorePagination(pageNum: 1, pageSize: 1){
                    pageNum
                    pageSize
                    totalPages
                    totalCount
                    scores { id }
                }
            }
            ''', headers=self.headers)
        res_03 = json.loads(response_03.content)["data"]
        self.assertResponseNoErrors(response_03)
        with self.subTest():
            self.assertEqual(res_03["scorePagination"]["totalPages"], 1)
            self.assertEqual(res_03["scorePagination"]["totalCount"], 1)
            self.assertEqual(res_03["scorePagination"]["scores"][0]["id"], 1)

        response_04 = self.query(
            '''
            {
                scoreCount(query: "id=1"){ count }
            }
            ''', headers=self.headers)
        res_04 = json.loads(response_04.content)["data"]
        self.assertResponseNoErrors(response_04)
        with self.subTest():
            self.assertEqual(res_04["scoreCount"]["count"], 1)

        response_05 = self.query(
            '''
            {
                scoreCount { count }
            }
            ''', headers=self.headers)
        res_05 = json.loads(response_05.content)["data"]
        self.assertResponseNoErrors(response_05)
        with self.subTest():
            self.assertEqual(res_05["scoreCount"]["count"], 1)

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
            ''', headers=self.headers)
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
            ''', headers=self.headers)
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
            ''', headers=self.headers)
        res = json.loads(response.content)["data"]
        self.assertResponseNoErrors(response)
        self.assertEqual(res["setScore"]["score"]["id"], 1)
    
    def test_delete_score(self):
        response = self.query(
            '''
            mutation {
                deleteScore(id:1) { id }
            }
            ''', headers=self.headers)
        res = json.loads(response.content)["data"]
        self.assertResponseNoErrors(response)
        self.assertEqual(res["deleteScore"]["id"], 1)

    def test_query_teams(self):
        response_01 = self.query(
            '''
            {
                teams(query: "id=1", orderBy: "id", limit: 1){
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
            ''', headers=self.headers)
        res_01 = json.loads(response_01.content)["data"]
        self.assertResponseNoErrors(response_01)
        with self.subTest():
            self.assertEqual(res_01["teams"][0]["id"], 1)

        response_02 = self.query(
            '''
            {
                teams{ id }
            }
            ''', headers=self.headers)
        res_02 = json.loads(response_02.content)["data"]
        self.assertResponseNoErrors(response_02)
        with self.subTest():
            self.assertEqual(res_02["teams"][0]["id"], 1)

        response_03 = self.query(
            '''
            {
                teamPagination(pageNum: 1, pageSize: 1){
                    pageNum
                    pageSize
                    totalPages
                    totalCount
                    teams { id }
                }
            }
            ''', headers=self.headers)
        res_03 = json.loads(response_03.content)["data"]
        self.assertResponseNoErrors(response_03)
        with self.subTest():
            self.assertEqual(res_03["teamPagination"]["totalPages"], 1)
            self.assertEqual(res_03["teamPagination"]["totalCount"], 1)
            self.assertEqual(res_03["teamPagination"]["teams"][0]["id"], 1)

        response_04 = self.query(
            '''
            {
                teamCount(query: "id=1"){ count }
            }
            ''', headers=self.headers)
        res_04 = json.loads(response_04.content)["data"]
        self.assertResponseNoErrors(response_04)
        with self.subTest():
            self.assertEqual(res_04["teamCount"]["count"], 1)

        response_05 = self.query(
            '''
            {
                teamCount { count }
            }
            ''', headers=self.headers)
        res_05 = json.loads(response_05.content)["data"]
        self.assertResponseNoErrors(response_05)
        with self.subTest():
            self.assertEqual(res_05["teamCount"]["count"], 1)

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
            ''', headers=self.headers)
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
            ''', headers=self.headers)
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
            ''', headers=self.headers)
        res = json.loads(response.content)["data"]
        self.assertResponseNoErrors(response)
        self.assertEqual(res["setTeam"]["team"]["id"], 1)
    
    def test_delete_team(self):
        response = self.query(
            '''
            mutation {
                deleteTeam(id:1) { id }
            }
            ''', headers=self.headers)
        res = json.loads(response.content)["data"]
        self.assertResponseNoErrors(response)
        self.assertEqual(res["deleteTeam"]["id"], 1)

    def test_query_users(self):
        response_01 = self.query(
            '''
            {
                users(query: "id=1", orderBy: "id", limit: 1){
                    id
                    username
                    firstName
                    lastName
                    email
                    isActive
                    teams {
                      id
                    }
                    profileImage {
                      id
                    }
                }
            }
            ''', headers=self.headers)
        res_01 = json.loads(response_01.content)["data"]
        self.assertResponseNoErrors(response_01)
        with self.subTest():
            self.assertEqual(res_01["users"][0]["id"], 1)

        response_02 = self.query(
            '''
            {
                users{ id }
            }
            ''', headers=self.headers)
        res_02 = json.loads(response_02.content)["data"]
        self.assertResponseNoErrors(response_02)
        with self.subTest():
            self.assertEqual(res_02["users"][0]["id"], 1)

        response_03 = self.query(
            '''
            {
                userPagination(pageNum: 1, pageSize: 1){
                    pageNum
                    pageSize
                    totalPages
                    totalCount
                    users { id }
                }
            }
            ''', headers=self.headers)
        res_03 = json.loads(response_03.content)["data"]
        self.assertResponseNoErrors(response_03)
        with self.subTest():
            self.assertEqual(res_03["userPagination"]["totalPages"], 1)
            self.assertEqual(res_03["userPagination"]["totalCount"], 1)
            self.assertEqual(res_03["userPagination"]["users"][0]["id"], 1)

        response_04 = self.query(
            '''
            {
                userCount(query: "id=1"){ count }
            }
            ''', headers=self.headers)
        res_04 = json.loads(response_04.content)["data"]
        self.assertResponseNoErrors(response_04)
        with self.subTest():
            self.assertEqual(res_04["userCount"]["count"], 1)

        response_05 = self.query(
            '''
            {
                userCount { count }
            }
            ''', headers=self.headers)
        res_05 = json.loads(response_05.content)["data"]
        self.assertResponseNoErrors(response_05)
        with self.subTest():
            self.assertEqual(res_05["userCount"]["count"], 1)

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
                    profileImage {
                      id
                    }
                }
            }
            ''', headers=self.headers)
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
                    profileImage: 1,
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
                        profileImage {
                          id
                        }
                    }
                }
            }
            ''', headers=self.headers)
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
                    profileImage: 1,

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
                        profileImage {
                          id
                        }
                    }
                }
            }
            ''', headers=self.headers)
        res = json.loads(response.content)["data"]
        self.assertResponseNoErrors(response)
        self.assertEqual(res["setUser"]["user"]["id"], 1)
    
    def test_delete_user(self):
        response = self.query(
            '''
            mutation {
                deleteUser(id:1) { id }
            }
            ''', headers=self.headers)
        res = json.loads(response.content)["data"]
        self.assertResponseNoErrors(response)
        self.assertEqual(res["deleteUser"]["id"], 1)