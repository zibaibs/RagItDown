from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
import os
from dotenv import load_dotenv

load_dotenv()


class Generator:
    def __init__(self, retriever):
        self.llm = ChatOpenAI(
            model="mistral-medium-3.5",
            api_key=os.getenv("MISTRAL_API_KEY"),
            base_url="https://api.mistral.ai/v1"
        )

        self.prompt = ChatPromptTemplate.from_template(""""
Answer the question based only on the following context:
{context}

Question: {question}
Answer:

Make sure to answer the question as concisely as possible, if you don't know the answer, just say that you don't know, don't try to make up an answer.
""")
        
        self.rag_chain = (
            {"context": retriever | self.format_docs, "question": RunnablePassthrough()}
            | self.prompt
            | self.llm
            | StrOutputParser()    
        )

    def format_docs(self, docs):
        return "\n".join([f"{doc.metadata['source']} - {doc.page_content}" for doc in docs])
    
    def answer(self, question: str) -> str:
        return self.rag_chain.invoke(question)