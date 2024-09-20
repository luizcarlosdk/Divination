from abc import ABC, abstractmethod

class LLMAnswerer(ABC):

    @abstractmethod
    def getAnswer(self, query, context, Settings):
        pass