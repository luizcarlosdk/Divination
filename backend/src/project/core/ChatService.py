class ChatService:
    def __init__(self, context_enricher, answerer, settings):
        self.context_enricher = context_enricher
        self.llm_answerer = answerer
        self.project_settings = settings

    def get_answer(self, query):
        
        context = self.context_enricher.getData(query)
        answer = self.llm_answerer.getAnswer(query, context, self.project_settings)
        
        return answer