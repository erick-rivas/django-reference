# Domains

Represents the methods to handle business logic

## Table of content

-  [Guidelines](#guidelines)
-  [Examples](#examples)
-  [References](#references)

##  Guidelines

-  To implement queries use query_util methods
    - Example: _get, _create, _list

##  Examples

```python
def create_project(user, project_name):  #

    # Use query_util methods to simplify requests
    # Example: (_get, _create, etc.)
    bmc_type = _get(CanvasType, type="BMC")
    project = _create(Project, name=project_name, description="description")
    c_types = _list(CanvasType)

    for c_type in c_types:
        project.add(_create(Canvas, type=c_type, project=project))
        _create(ProjectDetail, visibility="PUBLIC")
```

## References

-  Query reference: [https://docs.djangoproject.com/en/2.2/topics/db/queries/](https://docs.djangoproject.com/en/2.2/topics/db/queries/)
