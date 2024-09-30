Getting Started
---------------

1. **Install the package**: Follow the installation instructions above.
2. **Configure the middleware**: Add the middleware to your Django settings as shown in the configuration section.
3. **Run your Django application**: The middleware will automatically log HTTP requests and responses based on the configuration.
4. **Run Migrations**:
   - If you are using a separated database for logging, run:

     .. code-block:: sh

         python3 manage.py migrate dj_access_logger --database=logging

   - If you are using the same database, run:

     .. code-block:: sh

         python3 manage.py migrate dj_access_logger