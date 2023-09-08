"""
__Seed builder__
  (Read_only) Routes helper
"""

from rest_framework.renderers import BrowsableAPIRenderer as DRFBrowsableAPIRenderer

class BrowsableAPIRenderer(DRFBrowsableAPIRenderer):

    def get_context(self, *args, **kwargs):
        ctx = super().get_context(*args, **kwargs)
        is_dev_user = bool(ctx['user'] and ctx['user'].is_superuser)

        if not is_dev_user:
            ctx['display_edit_forms'] = False
            ctx['allowed_methods'] = []
            ctx['content'] = None
        return ctx

    def show_form_for_method(self, view, method, request, obj):
        return False

    def get_rendered_html_form(self, data, view, method, request):
        return ""