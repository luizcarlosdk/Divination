from project.ports.ContextEnricher import ContextEnricher
from project.adapters.OpenAILLM import OpenAILLM
from project.adapters.VectorDatabaseEnricher import VectorDatabaseEnricher
from project.core.ChatService import ChatService

def create_answer(query):

    context_enricher = VectorDatabaseEnricher()
    llm_answerer = OpenAILLM()
    service = ChatService(context_enricher,llm_answerer)
    answer = service.get_answer(query)
    
    return answer

resposta = create_answer("Give me the description of a barbarian")
print(resposta)