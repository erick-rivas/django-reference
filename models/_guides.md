# Models

Represents the model definitions of the application (database)

## Table of content

-   [Guidelines](#guidelines)
-   [Example](#example)
-   [References](#references)

## Guidelines

-   Modify attributes types and names via builder.
-   Only add aggregate methods (properties) if required
    -   Example: has_members(), complete_name() ...
-   To export a model use command \
>   $ seed export -m models:model_name

## Example

```python
class User(_User):  #
    @property
    def full_name(self):
        return self.first_name + " " + self.last_name
```

## References

-   Model reference: [https://docs.djangoproject.com/en/2.2/topics/db/models/](https://docs.djangoproject.com/en/2.2/topics/db/models/)
