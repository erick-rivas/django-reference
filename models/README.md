# Models

Represents the **extensions** of model definitions \
In most cases the entire models are generated automatically by seed-builder in (seed/models) folder

## Table of content

-   [Guidelines](#guidelines)
-   [Example](#example)
-   [References](#references)

## Guidelines

-   Modify attributes types and names via seed-builder.
-   Only add aggregate methods (properties) if required
    -   Example: has_members(), complete_name() ...
-   To extend a model use command
```bash
seed extend -m models:<model_name>
```

## Example

```python
class User(_User):  #
    @property
    def full_name(self):
        return self.first_name + " " + self.last_name
```

## References

-   Model reference: [https://docs.djangoproject.com/en/2.2/topics/db/models/](https://docs.djangoproject.com/en/2.2/topics/db/models/)