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

    # Use query_util to simplify requests
    # (_get, _create, etc.)
    bmc_type = _get(CanvasType, type="BMC")
    project = _create(Project, name=project_name, description="",
        canvas_type_2=bmc_type, admin=user)
    c_types = _get(CanvasType, type="")

    for c_type in c_types:
        project.add(_create(Canvas, type=c_type, project=project))
        _create(ProjectDetail, visibility="PUBLIC",
            industry="Innovation", location="México", website="None",
            total_sales=0, num_employees=0, num_investors=0, num_partnerships=0, num_patents=0,
            total_available_market=0, served_available_market=0, target_market=0,
            project=project)
```

## References

-  Query reference: [https://docs.djangoproject.com/en/2.2/topics/db/queries/](https://docs.djangoproject.com/en/2.2/topics/db/queries/)
