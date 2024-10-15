from project.ports.LLMAnswerer import LLMAnswerer
from project.core.RagChain import RagChain

from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

from langchain_core.prompts import PromptTemplate

import os


class OpenAILLM(LLMAnswerer):
    def getAnswer(self, query, context, settings):
        load_dotenv()
        os.environ["OPENAI_API_KEY"] = settings.security.OPENAI_API_KEY
        os.environ["LANGCHAIN_TRACING_V2"] = "true"
        os.environ["LANGCHAIN_API_KEY"] = settings.security.LANGCHAIN_API_KEY

        llm = ChatOpenAI(model="gpt-3.5-turbo-0125")

        custom_template = """Use the following pieces of context to answer the question at the end.
            If you don't know the answer, just say that you don't know, don't try to make up an answer.
            Give the answer keeping in mind that you are a dungeon master assistant and need to follow the context as much as possible.
            Always say "thanks for asking!" at the end of the answer.

        {context}

        Question: {question}

        Helpful Answer:"""

        custom_rag_prompt = PromptTemplate.from_template(custom_template)

        rag_chain = RagChain(context, custom_rag_prompt, llm, query)

        answer = rag_chain.answer(query)

        return answer
