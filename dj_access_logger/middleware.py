# python
import ipaddress

from django.utils.deprecation import MiddlewareMixin
from django.utils.timezone import now
from django.http import FileResponse

from dj_access_logger.repositories.repositories import RequestData, ResponseData, LogData


class AccessLogMiddleware(MiddlewareMixin):
    def process_request(self, request):
        request.start_time = now()
        # Read and store the request body to avoid multiple reads
        request._body = request.body if request.body else b''

    def process_response(self, request, response):
        try:
            request_body = request._body.decode('utf-8') if request._body else ''
        except UnicodeDecodeError:
            request_body = "<Binary Data>"

        if isinstance(response, FileResponse):
            response_data_content = "<File Response>"
        else:
            response_data_content = response.content.decode('utf-8') if response.content else ''

        request_data = RequestData(
            url=request.build_absolute_uri(),
            headers=dict(request.headers),
            data=request_body,
            method=request.method,
            ip_address=self.get_client_ip(request)[0],
            ipv4_address=self.get_client_ip(request)[1],
            ipv6_address=self.get_client_ip(request)[2],
            user_agent=request.META.get('HTTP_USER_AGENT', ''),
            referer=request.META.get('HTTP_REFERER', ''),
            session_data=dict(request.session.items()),
            cookies=request.COOKIES,
            query_params=request.GET,
            request_path=request.path,
            request_protocol=request.scheme,
            request_encoding=request.encoding,
            request_body_size=len(request_body)
        )

        response_data = ResponseData(
            headers=dict(response.items()),
            data=response_data_content,
            status_code=response.status_code,
            response_time=(now() - request.start_time).total_seconds(),
            response_body_size=len(response_data_content),
        )

        LogData(request=request_data, response=response_data).log()

        return response

    @staticmethod
    def get_client_ip(request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')

        ipv4_address = None
        ipv6_address = None

        try:
            ip_obj = ipaddress.ip_address(ip)
            if ip_obj.version == 4:
                ipv4_address = ip
            elif ip_obj.version == 6:
                ipv6_address = ip
                if ip_obj.ipv4_mapped:
                    ipv4_address = str(ip_obj.ipv4_mapped)
        except ValueError:
            pass

        return ip, ipv4_address, ipv6_address
