from abc import ABC, abstractmethod


class TemplateEnricher(ABC):
    @abstractmethod
    def getTemplate(self):
        pass
