from project.adapters.OpenAILLM import OpenAILLM
from project.adapters.VectorDatabaseEnricher import VectorDatabaseEnricher
from project.adapters.Settings import SecurityVariables

from project.core.ChatService import ChatService
from project.adapters.AnswerRouter import AnswerRouter

# ligar o fast api e passar as rotas
# usar o api/src/auraz/api.py de base
# uvicorn
# aiohttp
# _ = private
# instalar ruff como code formatter no vscode

def create_answer(query):

    context_enricher = VectorDatabaseEnricher()
    llm_answerer = OpenAILLM()
    settings = SecurityVariables()
    service = ChatService(context_enricher,llm_answerer,settings)

    router = AnswerRouter(service)