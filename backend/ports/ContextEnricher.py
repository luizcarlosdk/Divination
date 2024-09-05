from abc import ABC, abstractmethod

class ContextEnricher(ABC):

    @abstractmethod
    getData(self, query) -> Context:
        pass

    @abstractmethod
    getAnswer(self, query, context):
        pass