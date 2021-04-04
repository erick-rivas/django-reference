"""
__Seed builder__v0.2.0
  (Read_only) Builder helper
"""

from djangoql.admin import DjangoQLSearchMixin
from import_export import resources
from import_export.admin import ImportExportModelAdmin


class Resource(resources.ModelResource):
    class Meta:
        model = None


class ModelAdmin(DjangoQLSearchMixin, ImportExportModelAdmin):
    resource_class = None


# pylint: disable=C0103
def ModelAdminClass(model):
    resource_class = type('IEResource', (Resource,), {})
    meta = type('IEMeta', (), {})
    meta.model = model
    resource_class.Meta = meta
    model_admin = type('MAdmin', (ModelAdmin,), {})
    model_admin.resource_class = resource_class
    return model_admin