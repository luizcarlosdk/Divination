from project.ports.LLMAnswerer import LLMAnswerer
from project.core.RagChain import RagChain

from langchain_openai import ChatOpenAI
from langchain import hub
from dotenv import load_dotenv

import os


class OpenAILLM(LLMAnswerer):
    def getAnswer(self, query, context, settings):
        load_dotenv()
        os.environ["OPENAI_API_KEY"] = settings.security.OPENAI_API_KEY
        os.environ["LANGCHAIN_TRACING_V2"] = "true"
        os.environ["LANGCHAIN_API_KEY"] = settings.security.LANGCHAIN_API_KEY

        llm = ChatOpenAI(model="gpt-3.5-turbo-0125")
        prompt = hub.pull("rlm/rag-prompt")

        rag_chain = RagChain(context, prompt, llm, query)

        answer = rag_chain.answer(query)

        return answer
