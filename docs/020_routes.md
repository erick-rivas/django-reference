# Routes

Represents API routes (endpoints)

## Description

The routes are the responsible to handle all the http requests corresponding to a particular model

By default, the seed-builder generate the endpoints related to CRUD operations of a model. In case of extension new endpoints may be included in `routes/*py` files
>   *For more information see [seed-builder docs](060_seed_builder.md)*

## Extension examples

### GET example

```python
class PlayerViewSet(_PlayerViewSet):
    
    @action(detail=False, methods=['get'])
    def top_10(self, request):  #

        # Validate that has required fields
        has_fields_or_400(request.query_params, "category")
        category = request.query_params["category"]
        
        # Call domain methods
        players = get_top_players(category)

        # Return response (json)
        return this.response(players, many=True)
```

Endpoint
```bash
GET http://localhost:8000/players/top_10
```

### POST example

```python
class UserViewSet(_UserViewSet):
    
    @action(detail=True, methods=['post'])
    def create_profile(self, request, pk=None):  #
    
        # Get user or return 404 error
        # The pk param is obtained from endpoint. Example /user/:id
        user = get_object_or_404(_queryset(User), pk=pk)
 
        # Call domain methods
        create_profile(user)
        create_project(user, "Demo project")

        # Return response (json)
        return this.response(user, many=False)
```

Endpoint
```bash
POST http://localhost:8000/users/1/create_profile
```

## References

-   REST API explanation: [https://hackernoon.com/restful-api-designing-guidelines-the-best-practices-60e1d954e7c9](https://hackernoon.com/restful-api-designing-guidelines-the-best-practices-60e1d954e7c9)
-   Viewsets reference: [https://www.django-rest-framework.org/api-guide/viewsets/](https://www.django-rest-framework.org/api-guide/viewsets/)
-   Actions reference: [https://www.django-rest-framework.org/api-guide/viewsets/#viewset-actions](https://www.django-rest-framework.org/api-guide/viewsets/#viewset-actions)