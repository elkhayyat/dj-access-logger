Django Access Logger
====================

Django Access Logger is a middleware for logging HTTP requests and responses in Django applications. It supports logging to files, SQL databases, and NoSQL databases.

Features
--------

- Log HTTP requests and responses
- Support for file, SQL, and NoSQL logging
- Configurable via Django settings

Installation
------------

Install the package using pip:

.. code-block:: sh

    pip install dj-access-logger

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

Getting Started
---------------

1. **Install the package**: Follow the installation instructions above.
2. **Configure the middleware**: Add the middleware to your Django settings as shown in the configuration section.
3. **Run your Django application**: The middleware will automatically log HTTP requests and responses based on the configuration.

Logger Settings
---------------

Method
~~~~~~

The `method` setting determines how the logs are stored. It can be one of the following:

- `file`: Logs are stored in a file.
- `sql`: Logs are stored in an SQL database.
- `nosql`: Logs are stored in a NoSQL database.

Example:

.. code-block:: python

    DJ_ACCESS_LOGGER = {
        'method': 'file',  # or 'sql' or 'nosql'
    }

Separated Logging Database
~~~~~~~~~~~~~~~~~~~~~~~~~~

The `separated_logging_db` setting determines whether to use a separate database for logging.

Example:

.. code-block:: python

    DJ_ACCESS_LOGGER = {
        'separated_logging_db': True,
    }

Obfuscate Secrets
~~~~~~~~~~~~~~~~~

The `obfuscate_secrets` setting determines whether to obfuscate sensitive information in the logs.

Example:

.. code-block:: python

    DJ_ACCESS_LOGGER = {
        'obfuscate_secrets': True,
    }

Logging Database Parameters
~~~~~~~~~~~~~~~~~~~~~~~~~~~

The `logging_db_parameters` setting contains the database configuration for logging. This is required if `separated_logging_db` is set to `True`.

Example:

.. code-block:: python

    DJ_ACCESS_LOGGER = {
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

Usage
-----

The middleware will automatically log HTTP requests and responses based on the configuration.

License
-------

This project is licensed under the MIT License.