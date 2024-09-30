from dataclasses import dataclass
from typing import Dict, Any

from dj_access_logger.loggers.file_logger import FileLogger
from dj_access_logger.loggers.nosql_logger import NoSQLLogger
from dj_access_logger.loggers.sql_logger import SQLLogger
from dj_access_logger.utils import AccessLoggerSetting


@dataclass
class RequestData:
    url: str
    headers: Dict[str, Any]
    data: str | Dict
    method: str
    ip_address: str
    ipv4_address: str
    ipv6_address: str
    user_agent: str
    referer: str
    session_data: Dict[str, Any]
    cookies: Dict[str, Any]
    query_params: Dict[str, Any]
    request_path: str
    request_protocol: str
    request_encoding: str
    request_body_size: int


@dataclass
class ResponseData:
    headers: Dict[str, Any]
    data: str | Dict
    status_code: int
    response_time: float
    response_body_size: int


@dataclass
class LogData:
    request: RequestData
    response: ResponseData

    @property
    def settings(self):
        return AccessLoggerSetting()

    def get_logger(self):
        if self.settings.method == 'sql':
            return SQLLogger()
        elif self.settings.method == 'file':
            return FileLogger()
        elif self.settings.method == 'nosql':
            return NoSQLLogger()

    def log(self):
        self.get_logger().log(self)
