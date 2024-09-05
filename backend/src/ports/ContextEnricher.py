from abc import ABC, abstractmethod

class ContextEnricher(ABC):

    @abstractmethod
    def getData(self, query):
        pass

    @abstractmethod
    def getAnswer(self, query, context):
        pass