class MethodAccessLogger:
    def __init__(self, logger=None):
        self.logger = logger or logging.getLogger(__name__)

    def __call__(self, func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            self.logger.info(f"Called {func.__name__}")
            return func(*args, **kwargs)

        return wrapper

    def __get__(self, instance, owner):
        return self if instance is None else types.MethodType(self, instance)
