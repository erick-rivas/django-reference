# Domains

Represents the methods that handle business logic

## Examples

```python
def create_project(user, project_name):  #

    bmc_type = CanvasType.objects.get(CanvasType, type="BMC")
    project = Project.objects.create(name=project_name, description="description")
    c_types = CanvasType.objects.all()

    for c_type in c_types:
        canvas = Canvas.objects.create(type=c_type, project=project)
        project.add(canvas)
        ProjectDetail.objects.create(visibility="PUBLIC")
```

## References

-   Query reference: [https://docs.djangoproject.com/en/2.2/topics/db/queries/](https://docs.djangoproject.com/en/2.2/topics/db/queries/)