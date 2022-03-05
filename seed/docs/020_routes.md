# Routes

Represents API routes (endpoints)

## Description

By default, the seed-builder generates the endpoints related to CRUD operations of a model. 
-   In case of need custom endpoints, execute seed-builder command `seed-builder extend -m routes:<model_name>` and modify the generated file in `routes/<model_name>.py`
>   *For more information see [seed-builder docs](110_seed_builder.md)*

## Examples

### GET /players/top_10

```python
# routes/players.py
class PlayerViewSet(_PlayerViewSet):
    
    @action(detail=False, methods=['get'])
    def top_10(self, request):  #

        # Validate that has required fields
        has_fields_or_400(request.query_params, "category")
        category = request.query_params["category"]
        
        # Call domain methods
        players = get_top_players(category)

        # Return response (json)
        serializer = PlayerSerializer(players, many=True)
        return Response(serializer.data)
```

### POST /users/1/create_profile

```python
# routes/users.py
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
        serializer = UserSerializer(model, many=False)
        return Response(serializer.data)
```

## References

-   REST API explanation: [https://hackernoon.com/restful-api-designing-guidelines-the-best-practices-60e1d954e7c9](https://hackernoon.com/restful-api-designing-guidelines-the-best-practices-60e1d954e7c9)
-   Viewsets reference: [https://www.django-rest-framework.org/api-guide/viewsets/](https://www.django-rest-framework.org/api-guide/viewsets/)
-   Actions reference: [https://www.django-rest-framework.org/api-guide/viewsets/#viewset-actions](https://www.django-rest-framework.org/api-guide/viewsets/#viewset-actions)