# python
# dj_access_logger/apps.py

import os

from django.apps import AppConfig
from django.core.management import call_command

from .utils import DJ_ACCESS_LOGGER_SETTINGS


class DjAccessLoggerConfig(AppConfig):
    name = 'dj_access_logger'

    def ready(self):
        if DJ_ACCESS_LOGGER_SETTINGS.separated_logging_db:
            DJ_ACCESS_LOGGER_SETTINGS.set_separated_logging_db()
            if DJ_ACCESS_LOGGER_SETTINGS.logging_db_parameters.get('ENGINE') == 'django.db.backends.sqlite3':
                db_path = DJ_ACCESS_LOGGER_SETTINGS.logging_db_parameters.get('NAME', 'logging_db.sqlite3')
                if not os.path.exists(db_path):
                    print(f"Creating logging sqlite database at {db_path}")
                    open(db_path, 'w').close()
