"""
__Seed builder__
  (Read_only) Admin helper
"""

import json

from django import forms
from django.utils.html import html_safe

@html_safe
class JSPath:
    def __str__(self):
        return """
        <script>
            (function(){
                var $ = django.jQuery;
                $(document).ready(function(){
                    $('textarea.json-editor:not(.processed)').each(function(idx, el){
                        el.className += ' processed'
                        let editor = CodeMirror.fromTextArea(el, {
                            lineNumbers: true,
                            mode: {name: "javascript", json: true, statementIdent: 2},
                            indentUnit: 2
                        });
                        editor.setOption("extraKeys", {
                          Tab: function(cm) {
                            var spaces = Array(cm.getOption("indentUnit") + 1).join(" ");
                            cm.replaceSelection(spaces);
                          }
                        });
                    });
                });
            })();
        </script>
        """

    def startswith(self, data):
        pass

@html_safe
class CssPath:
    def __str__(self):
        return """
        <style>
            .CodeMirror {
                width: 100%
            }
        </style>
        """

    def startswith(self, data):
        pass

class JsonWidget(forms.Textarea):
    def __init__(self, *args, **kwargs):
        super(JsonWidget, self).__init__(*args, **kwargs)
        self.attrs['class'] = 'json-editor'

    # pylint: disable=W0702
    def format_value(self, value):
        try:
            return json.dumps(json.loads(value), indent=2)
        except:
            return value

    class Media:
        css = {
            'all': (
                'https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.9.0/codemirror.css',
                CssPath()
            )
        }
        js = (
            'https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.9.0/codemirror.js',
            'https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.9.0/mode/javascript/javascript.js',
            JSPath()
        )