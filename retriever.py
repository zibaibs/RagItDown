from langchain_chroma import Chroma
from langchain_mistralai.embeddings import MistralAIEmbeddings

class Retriever:
    def __init__(self, persist_directory = "chroma_db"):
        self.vector_store = Chroma(
            persist_directory=persist_directory, 
            embedding_function=MistralAIEmbeddings()
            )