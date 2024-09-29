from django.db import models


class AccessLog(models.Model):
    request_headers = models.JSONField()
    request_data = models.TextField()
    request_method = models.CharField(max_length=10)
    response_headers = models.JSONField()
    response_data = models.TextField()
    response_status_code = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Log {self.id} - {self.timestamp}"
