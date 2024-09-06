from project.ports.ContextEnricher import ContextEnricher

from langchain_community.document_loaders import TextLoader
from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter

class VectorDatabaseEnricher(ContextEnricher):

    def getData(self, query):
        loader = TextLoader("src/project/database/textobase.txt")
        documento = loader.load()

        text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
        splits = text_splitter.split_documents(documento)
        vectorstore = Chroma.from_documents(
        documents=splits,
        embedding=OpenAIEmbeddings(),
        persist_directory="../database/chroma_db",
        collection_name='vector_database')

        retriever = vectorstore.as_retriever()

        return retriever
    

 