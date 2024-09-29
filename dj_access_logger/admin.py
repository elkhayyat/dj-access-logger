# django_access_logger/admin.py

from django.contrib import admin

from .models import AccessLog


@admin.register(AccessLog)
class AccessLogAdmin(admin.ModelAdmin):
    list_display = ('id', 'timestamp', 'request_method', 'response_status_code')
    search_fields = ('request_headers', 'response_headers')
    list_filter = ('request_method', 'response_status_code')
