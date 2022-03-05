# Models

Represents project data entities (Database models)

## Description

By default, the seed-builder generate the models based on SeedManifest.json structure. In case of extension new attributes it may be included in `models/*.py` files
-   In case of need calculated attributes, \__str\__ overriding, etc. Execute seed-builder command `seed-builder extend -m models:<model_name>` and modify the generated file in `models/<model_name>.py`
>   *For more information see [seed-builder docs](110_seed_builder.md)*

## Example

```python
# models/user.py
class User(_User):
    @property
    def full_name(self):
        return self.first_name + " " + self.last_name
```

## Guidelines

-   Modify attributes types and names via seed-builder
-   Only add aggregate methods (properties) if required
    -   Example: has_members(), complete_name() ...

## References

-   Model reference: [https://docs.djangoproject.com/en/2.2/topics/db/models/](https://docs.djangoproject.com/en/2.2/topics/db/models/)