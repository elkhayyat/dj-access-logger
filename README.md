
# Django Access Logger

Django Access Logger is a middleware for logging HTTP requests and responses in Django applications. It supports logging to files, SQL databases, and NoSQL databases.

## Features

- Log HTTP requests and responses
- Support for file, SQL, and NoSQL logging
- Configurable via Django settings

## Installation

Install the package using pip:

```sh
pip install dj-access-logger
```

## Configuration

Add the middleware to your Django settings:

```python
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
ACCESS_LOGGER_METHOD = 'file'

# Database configuration for logging
DJANGO_ACCESS_LOGGER_DATABASE = {
    'ENGINE': 'django.db.backends.mysql',  # Use 'djongo' for MongoDB
    'NAME': 'logging_db',
    'USER': 'logging_user',
    'PASSWORD': 'logging_password',
    'HOST': 'localhost',
    'PORT': '3306',
    'NOSQL_HOST': 'mongodb://localhost:27017',  # NoSQL specific parameter
}
```

## Usage

The middleware will automatically log HTTP requests and responses based on the configuration.

## License

This project is licensed under the MIT License.
```
