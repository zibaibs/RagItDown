from markitdown import MarkItDown
from langchain_core.documents import Document
from langchain_text_splitters import MarkdownHeaderTextSplitter
from langchain_mistralai.embeddings import MistralAIEmbeddings
from langchain_chroma import Chroma
from dotenv import load_dotenv
import os

load_dotenv()

class Indexer:
    def __init__(self, persist_directory = "chroma_db"):
        self.persist_directory = persist_directory
        self.md = MarkItDown()
        self.embeddings = MistralAIEmbeddings()
        self.splitter = MarkdownHeaderTextSplitter(
            headers_to_split_on=[
                ("#", "titolo"),
                ("##", "sezione"),
                ("###", "sottosezione")
            ]
        )
    def _load_document(self, docs_path: str) -> list[Document]:
        documents = []
        for filename in os.listdir(docs_path):
            file_path = os.path.join(docs_path, filename)
            mardown_text = self.md.convert(file_path).text_content
            chuncks = self.splitter.split_text(mardown_text)
            for chunk in chuncks:
                chunk.metadata["source"] = filename
                documents.append(chunk)
        return documents
 
    def build_index(self, docs_path: str):
        documents = self._load_document(docs_path)
        return Chroma.from_documents(
            documents = documents,
            embedding = self.embeddings,
            persist_directory=self.persist_directory
        )
    
indexer = Indexer()
indexer.build_index("raw_data")
