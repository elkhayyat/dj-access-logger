DEFAULT_DJ_ACCESS_LOGGER = {
    "method": "file",
    "separated_logging_db": False,
    "obfuscate_secrets": True,
    "logging_db_parameters": {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'logging_db.sqlite3'
    }
}
