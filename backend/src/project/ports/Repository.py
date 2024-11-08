from abc import ABC, abstractmethod


class Repository(ABC):
    @abstractmethod
    def create(self, id):
        pass

    def get_history(self, id):
        pass
