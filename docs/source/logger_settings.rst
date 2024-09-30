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