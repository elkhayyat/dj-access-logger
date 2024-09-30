import json

from django.contrib import admin
from django.template.loader import render_to_string
from django.utils.html import format_html
from django.utils.safestring import mark_safe
from pygments import highlight, lexers, formatters

from .models import AccessLog


@admin.register(AccessLog)
class AccessLogAdmin(admin.ModelAdmin):
    list_display = ('id', 'timestamp', 'request_url', 'request_method', 'response_status_code', 'ip_address')
    search_fields = ('request_headers', 'response_headers')
    list_filter = (
    'request_url', 'request_method', 'response_status_code', 'ip_address', 'ipv4_address', 'ipv6_address')
    readonly_fields = (
        'id', 'timestamp', 'request_url', 'request_headers', 'request_data', 'request_method', 'response_headers',
        'response_data', 'response_status_code', 'session_data'
    )

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def request_headers(self, obj):
        return format_html(self.render_copyable_field(obj.request_headers))

    def request_data(self, obj):
        return format_html(self.render_copyable_field(obj.request_data))

    def response_headers(self, obj):
        return format_html(self.render_copyable_field(obj.response_headers))

    def response_data(self, obj):
        return format_html(self.render_response_data(obj.response_data, obj.response_headers))

    def session_data(self, obj):
        return format_html(self.render_copyable_field(obj.session_data))

    @staticmethod
    def render_copyable_field(self, value):  # https://daniel.feldroy.com/posts/pretty-formatting-json-django-admin#
        """Function to display pretty version of our data"""
        # Convert the data to sorted, indented JSON
        response = json.dumps(value, sort_keys=True, indent=2)
        # Truncate the data. Alter as needed
        # response = response[:5000]
        # Get the Pygments formatter
        formatter = formatters.HtmlFormatter(style='staroffice', linenos='table')  # pylint: disable=no-member
        # Highlight the data
        response = highlight(response, lexers.JsonLexer(), formatter)  # pylint: disable=no-member
        # Get the stylesheet
        style = "<style>" + formatter.get_style_defs() + "</style><br>"

        copy_button = """
            <script>
                window.onCopyCodeButtonClick = function(element) {
                    let codeContainer = element.parentElement.getElementsByClassName("code")[0];
                    navigator.clipboard.writeText(codeContainer.innerText);
                }
            </script>
            <button type="button" onclick="onCopyCodeButtonClick(this)" title="Copy">Copy JSON</button>
        """

        # Safe the output
        return mark_safe(style + response + copy_button)

    def render_response_data(self, response_data, response_headers):
        content_type = response_headers.get('Content-Type', '')
        if 'application/json' in content_type:
            formatted_value = json.dumps(json.loads(response_data), indent=4)
            return render_to_string('admin/copyable_field.html', {'value': formatted_value})
        elif 'text/html' in content_type:
            return format_html(response_data)
        elif 'exception' in response_data.lower():
            return format_html('<pre>{}</pre>', response_data)
        else:
            return format_html('<div style="white-space: pre-wrap;">{}</div>', response_data)
