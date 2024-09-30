# python

from django.db import models


class AccessLog(models.Model):
    id = models.AutoField(primary_key=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    request_url = models.CharField(max_length=200)
    request_headers = models.JSONField()
    request_data = models.TextField()
    request_method = models.CharField(max_length=10)
    response_headers = models.JSONField()
    response_data = models.TextField()
    response_status_code = models.IntegerField()
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    ipv4_address = models.GenericIPAddressField(null=True, blank=True)
    ipv6_address = models.GenericIPAddressField(null=True, blank=True)
    user_agent = models.CharField(max_length=255, null=True, blank=True)
    referer = models.CharField(max_length=255, null=True, blank=True)
    session_data = models.JSONField(null=True, blank=True)
    cookies = models.JSONField(null=True, blank=True)
    query_params = models.JSONField(null=True, blank=True)
    request_path = models.CharField(max_length=255, null=True, blank=True)
    request_protocol = models.CharField(max_length=10, null=True, blank=True)
    request_encoding = models.CharField(max_length=50, null=True, blank=True)
    response_time = models.FloatField(null=True, blank=True)
    request_body_size = models.IntegerField(null=True, blank=True)
    response_body_size = models.IntegerField(null=True, blank=True)
    response_is_ok = models.BooleanField(default=False)

    def __str__(self):
        return f'AccessLog {self.id}'
