print("This is the mainfile,test")

from project.ports.ContextEnricher import ContextEnricher
from project.adapters.OpenAILLM import OpenAILLM
from project.adapters.VectorDatabaseEnricher import VectorDatabaseEnricher


class ChatService:
    def __init__(self):
        self.enricher = VectorDatabaseEnricher()
        self.llm = OpenAILLM()

    def getAnswer(self, query):

        context = self.enricher.getData(query)
        answer =  self.llm.getAnswer(query, context)

        return answer



chatservice = ChatService()

resposta = chatservice.getAnswer("Tell me about the barbarian class on level 3")
print(resposta)