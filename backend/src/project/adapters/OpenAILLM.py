from project.ports.LLMAnswerer import LLMAnswerer
from project.core.RagChain import RagChain

from langchain_openai import ChatOpenAI
from dotenv import load_dotenv


import os


class OpenAILLM(LLMAnswerer):
    def getAnswer(self, query, context, template, settings):
        load_dotenv()
        os.environ["OPENAI_API_KEY"] = settings.security.OPENAI_API_KEY
        os.environ["LANGCHAIN_TRACING_V2"] = "true"
        os.environ["LANGCHAIN_API_KEY"] = settings.security.LANGCHAIN_API_KEY

        llm = ChatOpenAI(model="gpt-3.5-turbo-0125")

        rag_chain = RagChain(context, template, llm, query)

        answer = rag_chain.answer(query)

        return answer
