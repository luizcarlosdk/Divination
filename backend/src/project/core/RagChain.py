from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough

class RagChain():
    def __init__(self,context,prompt,llm,query):
        self.context = context
        self.prompt = prompt
        self.llm = llm

    def answer(query):

        rag_chain = (
            {"context": self.context, "question": RunnablePassthrough()}
            | self.prompt
            | self.llm
            | StrOutputParser()
        )
        
        answer = rag_chain.invoke(query)

        return answer