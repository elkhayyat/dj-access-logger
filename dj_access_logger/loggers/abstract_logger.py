from abc import ABC, abstractmethod
from .singleton import SingletonABCMeta

class AbstractLogger(ABC, metaclass=SingletonABCMeta):
    @abstractmethod
    def log(self, log_data):
        pass