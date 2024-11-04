class ChatService:
    def __init__(
        self, context_enricher, answerer, template, chat_repository, settings
    ):
        self.context_enricher = context_enricher
        self.llm_answerer = answerer
        self.answer_template = template
        self.chat_repository = chat_repository
        self.project_settings = settings

    def get_answer(self, query, chat_id):
        context = self.context_enricher.getData(query)
        chat = self.chat_repository.getHistory(chat_id, max=10)
        template = self.answer_template.getTemplate()
        answer = self.llm_answerer.getAnswer(
            query, context, chat, template, self.project_settings
        )

        return answer

    # def create chat


# na requisição vamos receber

# id do usuário - pensar em como criar
# personalidade do bot
# pergunta
# id da conversa
#
# chat service vai ser responsável por criar um novo chat
