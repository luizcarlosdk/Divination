from project.ports.enrichers.TemplateEnricher import TemplateEnricher
from typing import Optional
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder


class AnswerEnricher(TemplateEnricher):
    def __init__(
        self,
        template: Optional[str] = None,
        history_template: Optional[str] = None,
    ):
        if template is None:
            with open(
                "src/project/database/templates/defaultTemplate.txt", "r"
            ) as defaultTemplate:
                self.template = defaultTemplate.read()
        else:
            self.template = template

        if history_template is None:
            with open(
                "src/project/database/templates/contextualized_prompt_template.txt",
                "r",
            ) as historyTemplate:
                self.history_template = historyTemplate.read()
        else:
            self.history_template = history_template

    def get_template(self):
        custom_template = ChatPromptTemplate(
            [
                ("system", self.template),
                MessagesPlaceholder("chat_history"),
                ("human", "{input}"),
            ]
        )
        return custom_template

    def get_history_template(self):
        custom_template = ChatPromptTemplate(
            [
                ("system", self.history_template),
                MessagesPlaceholder("chat_history"),
                ("human", "{input}"),
            ]
        )
        return custom_template

    def change_template(self, new_template):
        path = ""
        if new_template == "default":
            path = "src/project/database/templates/defaultTemplate.txt"
        elif new_template == "creative":
            path = "src/project/database/templates/creativeTemplate.txt"
        else:
            return "personalidade não encontrada"
        print("path de personalidade atual:" + path)
        with open(path) as new_personality:
            self.template = new_personality.read()
