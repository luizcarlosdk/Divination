class ChatService:
    def __init__(self, context_enricher, answerer, template, settings):
        self.context_enricher = context_enricher
        self.llm_answerer = answerer
        self.answer_template = template
        self.project_settings = settings

    def get_answer(self, query):
        context = self.context_enricher.getData(query)
        template = self.answer_template.getTemplate()
        answer = self.llm_answerer.getAnswer(
            query, context, template, self.project_settings
        )

        return answer
