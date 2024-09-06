from project.ports.LLMAnswerer import LLMAnswerer

from langchain_openai import ChatOpenAI
from langchain import hub
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from dotenv import load_dotenv

import getpass
import os


class OpenAILLM(LLMAnswerer):

    def getAnswer(self,query,context):

        load_dotenv()
        os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
        os.environ["LANGCHAIN_TRACING_V2"] = "true"
        os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
        llm = ChatOpenAI(model="gpt-3.5-turbo-0125")
        prompt = hub.pull("rlm/rag-prompt")

        rag_chain = (
            {"context": context, "question": RunnablePassthrough()}
            | prompt
            | llm
            | StrOutputParser()
        )
        answer = rag_chain.invoke(query)

        return answer