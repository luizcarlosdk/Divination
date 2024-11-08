from project.ports.LLMAnswerer import LLMAnswerer

from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

from langchain.chains import (
    create_history_aware_retriever,
    create_retrieval_chain,
)
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.runnables.history import RunnableWithMessageHistory

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

        llm = ChatOpenAI(model="gpt-3.5-turbo-0125")

        history_retriever = create_history_aware_retriever(
            llm, context, history_template
        )

        question_answer_chain = create_stuff_documents_chain(llm, template)

        rag_chain = create_retrieval_chain(
            history_retriever, question_answer_chain
        )

        conversational_rag_chain = RunnableWithMessageHistory(
            rag_chain,
            chat_repository.get_history,
            input_messages_key="input",
            history_messages_key="chat_history",
            output_messages_key="answer",
        )

        answer = conversational_rag_chain.invoke(
            {"input": query},
            config={"configurable": {"session_id": chat_id}},
        )["answer"]

        return answer
