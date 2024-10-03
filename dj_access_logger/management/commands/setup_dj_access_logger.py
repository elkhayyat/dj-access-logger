# dj_access_logger/management/commands/setup_dj_access_logger.py

from django.apps import apps
from django.core.management.base import BaseCommand
from django.db import connections
from django.db.migrations.executor import MigrationExecutor


class Command(BaseCommand):
    help = 'Set up the logging database for dj_access_logger'

    def handle(self, *args, **options):
        self.stdout.write("Setting up logging database...")

        # Get the logging database connection
        connection = connections['logging']

        # Check if there are any tables in the database
        with connection.cursor() as cursor:
            cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
            tables = cursor.fetchall()

        if not tables:
            self.stdout.write("No tables found. Creating tables...")

            # Get the app's migration operations
            app_config = apps.get_app_config('dj_access_logger')
            migration_executor = MigrationExecutor(connection)
            targets = [(app_config.label, None)]

            # Run the migrations
            migration_executor.migrate(targets)

            self.stdout.write(self.style.SUCCESS("Successfully created tables for dj_access_logger."))
        else:
            self.stdout.write("Tables already exist in the logging database.")

        self.stdout.write(self.style.SUCCESS("Logging database setup complete."))
