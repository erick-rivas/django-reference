"""
__Seed builder__
  (Read_only) Admin helper
"""

from django import forms

from django.utils.html import html_safe

@html_safe
class JSPath:
    def __str__(self):
        return """
        <script>
            (function(){
                $(document).ready(function(){
                    $('textarea.code-editor:not(.processed)').each(function(idx, el){
                        el.className += ' processed'
                        let editor = CodeMirror.fromTextArea(el, {
                            lineNumbers: true,
                            mode: "python",
                            indentUnit: 4
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

class CodeWidget(forms.Textarea):
    def __init__(self, *args, **kwargs):
        super(CodeWidget, self).__init__(*args, **kwargs)
        self.attrs['class'] = 'code-editor'

    class Media:
        css = {
            'all': (
                'https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.9.0/codemirror.css',
                CssPath()
            )
        }
        js = (
            'https://cdnjs.cloudflare.com/ajax/libs/jquery/3.7.1/jquery.min.js',
            'https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.9.0/codemirror.js',
            'https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.9.0/mode/python/python.js',
            JSPath()
        )