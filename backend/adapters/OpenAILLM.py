from ../ports import ContextEnricher

def openAILLM(ContextEnricher):

    def getAnswer(self,query,context):
        prompt = hub.pull("rlm/rag-prompt")

        rag_chain = (
            {"context": context, "question": RunnablePassthrough()}
            | prompt
            | llm
            | StrOutputParser()
        )

        answer = rag_chain.invoke(query)

        return answer