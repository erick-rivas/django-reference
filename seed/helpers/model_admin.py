"""
__Seed builder__v0.1.8
  (Read_only) Builder helper
"""

from import_export.admin import ImportExportModelAdmin
from import_export import resources
from djangoql.admin import DjangoQLSearchMixin
        
class Resource(resources.ModelResource):
    class Meta:
        model = None

class ModelAdmin(DjangoQLSearchMixin, ImportExportModelAdmin):
    resource_class = None

def ModelAdminClass(model):  #

    resource_class = type('IEResource', (Resource,), {})
    meta = type('IEMeta', (), {})
    meta.model = model
    resource_class.Meta = meta
    model_admin = type('MAdmin', (ModelAdmin,), {})
    model_admin.resource_class = resource_class
    return model_admin