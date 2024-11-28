from abc import ABC, abstractmethod

class Router(ABC):

    @abstractmethod
    def create(self):
        pass