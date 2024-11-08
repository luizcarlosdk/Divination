from project.ports.TemplateEnricher import TemplateEnricher
from typing import Optional
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder


class AnswerTemplate(TemplateEnricher):
    def __init__(
        self,
        template: Optional[str] = None,
        history_template: Optional[str] = None,
    ):
        if template is None:
            with open(
                "src/project/database/defaultTemplate.txt", "r"
            ) as defaultTemplate:
                self.template = defaultTemplate.read()
        else:
            self.template = template

        if history_template is None:
            with open(
                "src/project/database/contextualized_prompt.txt", "r"
            ) as historyTemplate:
                self.history_template = historyTemplate.read()
        else:
            self.history_template = history_template

    def get_template(self):
        custom_template = ChatPromptTemplate.from_messages(
            [
                ("system", self.template),
                MessagesPlaceholder("chat_history"),
                ("human", "{input}"),
            ]
        )
        return custom_template

    def get_history_template(self):
        custom_template = ChatPromptTemplate.from_messages(
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
            path = "src/project/database/defaultTemplate.txt"
        elif new_template == "creative":
            path = "src/project/database/creativeTemplate.txt"
        else:
            return "personalidade não encontrada"
        with open(path) as new_personality:
            self.template = new_personality.read()
