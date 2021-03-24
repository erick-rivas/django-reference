# Models

Represents data model representation (Database models)


## Description

The models  are responsible to represent data storage including database mapping

By default, the seed-builder generate the models based on SeedManifest.json structure. In case of extension new attributes it may be included in `models/*.py` files
>   *For more information see [seed-builder docs](060_seed_builder.md)*


## Extension Example

```python
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