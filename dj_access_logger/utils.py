from django.conf import settings

from .default_settings import DEFAULT_DJ_ACCESS_LOGGER


class AccessLoggerSetting:
    def __init__(self):
        user_settings = getattr(settings, 'DJ_ACCESS_LOGGER', {})
        self.method = user_settings.get("method", DEFAULT_DJ_ACCESS_LOGGER["method"])
        self.separated_logging_db = user_settings.get("separated_logging_db",
                                                      DEFAULT_DJ_ACCESS_LOGGER["separated_logging_db"])
        self.obfuscate_secrets = user_settings.get("obfuscate_secrets", DEFAULT_DJ_ACCESS_LOGGER["obfuscate_secrets"])
        self.logging_db_parameters = user_settings.get("logging_db_parameters",
                                                       DEFAULT_DJ_ACCESS_LOGGER["logging_db_parameters"])
        if self.separated_logging_db:
            self.set_separated_logging_db()
        self.validate()

    def set_separated_logging_db(self):
        settings.DATABASES['logging'] = self.logging_db_parameters
        if isinstance(settings.DATABASE_ROUTERS, tuple):
            settings.DATABASE_ROUTERS = list(settings.DATABASE_ROUTERS)
        if not isinstance(settings.DATABASE_ROUTERS, list):
            settings.DATABASE_ROUTERS = []
        settings.DATABASE_ROUTERS.append('dj_access_logger.db_router.LoggingDBRouter')

    def validate(self):
        if self.method not in ['file', 'sql', 'nosql']:
            raise ValueError("DJ_ACCESS_LOGGER['method'] must be 'file', 'sql' or 'nosql'")

        if self.method == 'nosql' and not self.logging_db_parameters:
            raise ValueError("DJ_ACCESS_LOGGER['logging_db_parameters'] must be set for 'nosql' method")


DJ_ACCESS_LOGGER_SETTINGS = AccessLoggerSetting()
