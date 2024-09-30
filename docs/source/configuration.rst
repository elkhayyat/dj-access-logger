Configuration
-------------

Add the middleware to your Django settings:

.. code-block:: python

    # settings.py
    INSTALLED_APPS = [
        ...
        'dj_access_logger'
        ...
    ]

    MIDDLEWARE = [
        ...
        'dj_access_logger.middleware.AccessLoggerMiddleware',
        ...
    ]

    # Logging method: 'file', 'sql', or 'nosql'
    DJ_ACCESS_LOGGER = {
        'method': 'file',  # 'file' or 'sql' or 'nosql'
        'separated_logging_db': True,
        'obfuscate_secrets': True,
        'logging_db_parameters': {
            'ENGINE': 'django.db.backends.mysql',  # Use 'djongo' for MongoDB
            'NAME': 'logging_db',
            'USER': 'logging_user',
            'PASSWORD': 'logging_password',
            'HOST': 'localhost',
            'PORT': '3306',
            'NOSQL_HOST': 'mongodb://localhost:27017',  # NoSQL specific parameter
        }
    }