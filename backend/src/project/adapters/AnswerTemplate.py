from project.ports.TemplateEnricher import TemplateEnricher
from langchain_core.prompts import PromptTemplate
from typing import Optional


class AnswerTemplate(TemplateEnricher):
    def __init__(self, template: Optional[str] = None):
        if template is None:
            with open(
                "src/project/database/defaultTemplate.txt", "r"
            ) as defaultTemplate:
                self.template = defaultTemplate.read()
        else:
            self.template = template

    def getTemplate(self):
        custom_template = PromptTemplate.from_template(self.template)
        return custom_template

    def changeTemplate(self, new_template):
        self.template = new_template
