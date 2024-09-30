# python
import json

from .abstract_logger import AbstractLogger


class FileLogger(AbstractLogger):
    def log(self, log_data):
        response_status_code = log_data.response.status_code
        response_is_ok = 200 <= response_status_code < 300
        log_entry = {
            'request_url': log_data.request.url,
            'request_headers': log_data.request.headers,
            'request_data': log_data.request.data,
            'request_method': log_data.request.method,
            'response_headers': log_data.response.headers,
            'response_data': log_data.response.data,
            'response_status_code': response_status_code,
            'ip_address': log_data.request.ip_address,
            'user_agent': log_data.request.user_agent,
            'referer': log_data.request.referer,
            'session_data': log_data.request.session_data,
            'cookies': log_data.request.cookies,
            'query_params': log_data.request.query_params,
            'request_path': log_data.request.request_path,
            'request_protocol': log_data.request.request_protocol,
            'request_encoding': log_data.request.request_encoding,
            'response_time': log_data.response.response_time,
            'request_body_size': log_data.request.data,
            'response_body_size': log_data.response.response_body_size,
            'response_is_ok': response_is_ok
        }

        with open('access_log.json', 'a') as log_file:
            log_file.write(json.dumps(log_entry) + '\n')
