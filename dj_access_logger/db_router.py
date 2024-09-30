class LoggingDBRouter:
    """
    A router to control all database operations on models in the
    dj_access_logger application.
    """

    def db_for_read(self, model, **hints):
        """
        Attempts to read dj_access_logger models go to logging_db.
        """
        if model._meta.app_label == 'dj_access_logger':
            return 'logging'
        return None

    def db_for_write(self, model, **hints):
        """
        Attempts to write dj_access_logger models go to logging_db.
        """
        if model._meta.app_label == 'dj_access_logger':
            return 'logging'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the dj_access_logger app is involved.
        """
        if obj1._meta.app_label == 'dj_access_logger' or \
                obj2._meta.app_label == 'dj_access_logger':
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Make sure the dj_access_logger app only appears in the 'logging_db'
        database.
        """
        if app_label == 'dj_access_logger':
            return db == 'logging'
        return None
