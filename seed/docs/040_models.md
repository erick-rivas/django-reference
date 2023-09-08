# Models

Represents project data entities (Database models)

## Description

By default, the seed-builder generate the models based on SeedManifest.json structure. In case of extension new attributes, permissions, etc. it may be included in `models/*.py` files

## Non-stored fields (Properties)
In case of need fields that can be used but not stored (e.g calculated attributes, \__str\__ overriding).
Execute seed-builder command `seed-builder extend -m models:<model_name>` and modify the generated file in `models/<model_name>.py`
>   *For more information see [seed-builder docs](110_seed_builder.md)*

## Example

```python
# models/child.py
class Child(_Child):
    @property
    def full_name(self):
        return self.first_name + " " + self.last_name
```

## Permissions

Permissions are queryset filters integrated in the model to limit object access in API and graphql requests.
Note: In order to modify permissions, it is necessary to previously extend the model with the command `seed-builder extend -m models:<model_name>`

Example: For `User -> Child`
```python
# models/child.py
class Child(_User):
    # It integrate the filter .filter(user=REQUEST_USER) to all the API and Graphql requests
    @staticmethod
    def permission_filters(user):
        return {"user": user}
```

In case of need perms of grandparent models, it can be use the `inherit_permissions` method

Example: For `User -> Child -> Grandson`
```python
# models/child.py
class Grandson(_User):
    # It concatenate the filter of Child with Grandson
    # For this example, the permissions would be equivalent to integrating .filter(user__parent=user)
    # to all the API and Graphql requests
    @staticmethod
    def permission_filters(user):
        from app.models import Child
        return Grandson.inherit_permissions(Child, "parent", user)
```

For complex cases, it can also include multiple permissions

Example: For `User -> Node_A` and `User -> Node_B -> Node_A`
```python
# models/child.py
class Node_A(_User):
    # For this example, the permissions would be equivalent to integrating .filter(user=user, <NODE_B_PERMS>__node_b=user)
    @staticmethod
    def permission_filters(user):
        from app.models import Node_B
        return {
            "user": user
            Node_A.inherit_permissions(Node_B, "node_b", user)
        }
```

## Guidelines

-   Modify attributes types and names via seed-builder
-   Only add aggregate methods (properties) if required
    -   Example: has_members(), complete_name() ...

## References

-   Model reference: [https://docs.djangoproject.com/en/2.2/topics/db/models/](https://docs.djangoproject.com/en/2.2/topics/db/models/)