# dj_access_logger/db_router.py

class LoggingDBRouter:
    """
    A router to control all database operations on models in the
    dj_access_logger application.
    """

    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'dj_access_logger':
            return 'logging'
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'dj_access_logger':
            return 'logging'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        if obj1._meta.app_label == 'dj_access_logger' or obj2._meta.app_label == 'dj_access_logger':
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label == 'dj_access_logger':
            return db == 'logging'
        elif db == 'logging':
            return app_label == 'dj_access_logger'
        return None

    def allow_syncdb(self, db, model):
        if model._meta.app_label == 'dj_access_logger':
            return db == 'logging'
        elif db == 'logging':
            return model._meta.app_label == 'dj_access_logger'
        return None

    def connection_allows_schema_migrate(self, connection, app_label):
        if app_label == 'dj_access_logger':
            return connection.alias == 'logging'
        return None
