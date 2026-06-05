import gradio as gr
from indexer import Indexer
from retriever import Retriever
from generator import Generator
import os
from dotenv import load_dotenv
from langchain_mistralai.embeddings import MistralAIEmbeddings
from langchain_openai import ChatOpenAI
import shutil

load_dotenv()


INDEX_PATH = "chroma_db"
DOCS_PATH = "raw_data"

if os.path.exists(INDEX_PATH):
    shutil.rmtree(INDEX_PATH)
    
indexer = Indexer()
indexer.build_index(DOCS_PATH)

retriever = Retriever().retriever
generator = Generator(retriever)

def chat(message, history):
    return generator.answer(message)

demo = gr.ChatInterface(
    fn=chat,
    title= "RagItDown - AI RAG Chatbot",
    description="Ask me anything about the documents in the raw_data folder!"
)

if __name__ == "__main__":
    demo.launch()