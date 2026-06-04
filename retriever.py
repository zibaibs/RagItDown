from langchain_chroma import Chroma
from langchain_mistralai.embeddings import MistralAIEmbeddings
from dotenv import load_dotenv
import os

load_dotenv()

class Retriever:
    def __init__(self, persist_directory = "chroma_db"):
        self.vector_store = Chroma(
            persist_directory=persist_directory, 
            embedding_function=MistralAIEmbeddings()
            )
        self.retriever = self.vector_store.as_retriever(
            search_type="similarity",
            search_kwargs={"k": 3}
        )
    
    def search(self, query: str, k: int = 3) -> list[str]:
        results = self.vector_store.similarity_search(query, k=k)
        return [doc.page_content for doc in results]
    