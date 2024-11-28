from project.ports.answerers.LLMAnswerer import LLMAnswerer
from project.core.RagChain import RagChain
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain.chains import create_history_aware_retriever
from langchain.chains.combine_documents import create_stuff_documents_chain
import os


class OpenAILLM(LLMAnswerer):
    def get_answer(
        self,
        chat_id,
        query,
        context,
        chat_repository,
        template,
        history_template,
        settings,
    ):
        load_dotenv()
        os.environ["OPENAI_API_KEY"] = settings.security.OPENAI_API_KEY
        os.environ["LANGCHAIN_TRACING_V2"] = "true"
        os.environ["LANGCHAIN_API_KEY"] = settings.security.LANGCHAIN_API_KEY

        llm = ChatOpenAI(model="gpt-4o-mini")

        history_retriever = create_history_aware_retriever(
            llm, context, history_template
        )

        question_answer_chain = create_stuff_documents_chain(llm, template)

        ragchain = RagChain(
            chat_repository, history_retriever, question_answer_chain
        )
        answer = ragchain.answer(query, chat_id)

        return answer
