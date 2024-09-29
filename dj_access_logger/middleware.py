# django_access_logger/middleware.py

import json
import logging

from django.conf import settings
from django.utils.deprecation import MiddlewareMixin

from .models import AccessLog

logger = logging.getLogger(__name__)


class AccessLoggerMiddleware(MiddlewareMixin):
    def process_request(self, request):
        request._body = request.body
        request._headers = request.headers

    def process_response(self, request, response):
        if getattr(settings, 'ACCESS_LOGGER_OBFUSCATE_SECRETS', True):
            request_data = self._obfuscate_secrets(request._body)
            response_data = self._obfuscate_secrets(response.content)
        else:
            request_data = request._body
            response_data = response.content

        log_data = {
            'request': {
                'headers': dict(request._headers),
                'data': request_data.decode('utf-8') if request_data else '',
                'method': request.method,
            },
            'response': {
                'headers': dict(response.items()),
                'data': response_data.decode('utf-8') if response_data else '',
                'status_code': response.status_code,
            }
        }

        if settings.ACCESS_LOGGER_METHOD == 'file':
            logger.info(json.dumps(log_data, indent=2))
        elif settings.ACCESS_LOGGER_METHOD == 'sql':
            AccessLog.objects.create(
                request_headers=log_data['request']['headers'],
                request_data=log_data['request']['data'],
                request_method=log_data['request']['method'],
                response_headers=log_data['response']['headers'],
                response_data=log_data['response']['data'],
                response_status_code=log_data['response']['status_code']
            )
        elif settings.ACCESS_LOGGER_METHOD == 'nosql':
            from pymongo import MongoClient
            client = MongoClient(settings.DJANGO_ACCESS_LOGGER_DATABASE['NOSQL_HOST'])
            db = client[settings.DJANGO_ACCESS_LOGGER_DATABASE['NAME']]
            db.access_logs.insert_one(log_data)

        return response

    def _obfuscate_secrets(self, data):
        try:
            data_dict = json.loads(data)
            if 'password' in data_dict:
                data_dict['password'] = '****'
            if 'Authorization' in data_dict:
                data_dict['Authorization'] = '****'
            return json.dumps(data_dict).encode('utf-8')
        except (ValueError, TypeError):
            return data
