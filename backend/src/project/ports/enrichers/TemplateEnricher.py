from abc import ABC, abstractmethod


class TemplateEnricher(ABC):
    @abstractmethod
    def get_template(self):
        pass
