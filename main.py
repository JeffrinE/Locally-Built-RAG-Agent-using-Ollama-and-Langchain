import os
from langchain_community.document_loaders import DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import Weaviate

import weaviate
from langchain.prompts import ChatPromptTemplate
from weaviate.embedded import EmbeddedOptions
from langchain.chains.question_answering import load_qa_chain
from langchain_community.llms import OpenAI
from langchain_community.chat_models import ChatOpenAI

from langchain.schema.runnable import RunnablePassthrough
from langchain.schema.output_parser import StrOutputParser
from langchain_community.document_loaders import PyPDFLoader

import google.generativeai as genai
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_google_genai import ChatGoogleGenerativeAI

from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.chat_models import ChatOllama
from langchain_community.vectorstores import Chroma

from langchain_community.document_loaders import TextLoader
from langchain_community.vectorstores import FAISS
from langchain.chains import RetrievalQA

directory = r'C:\Users\File_Path_To_Pdf'

def load_docs(directory):
    loader = PyPDFLoader(directory)
    documents = loader.load()
    return documents

documents = load_docs(directory)

from langchain.text_splitter import RecursiveCharacterTextSplitter

def split_documents(documents, chunk_size=1000, chunk_overlap=20):
    text_split = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    chunks = text_split.split_documents(documents)
    return chunks


chunks = split_documents(documents)
print(f"Total number of chunks: {len(chunks)}")
print("\n")
embeddings = OllamaEmbeddings(model="embedding-model-here") #Replace model with your preferred embedding model

db = Chroma.from_documents(chunks, embeddings, collection_name = "local-rag")

retriever = db.as_retriever()

template = """You are an assistant for question-answering tasks.
Use the following pieces of retrieved context to answer the question:
If you don't know the answer, then answer from your own knowledge and dont give just one word answer, and dont tell the user that you are answering from your knowledge.
Use three sentences maximum and keep the answer concise.

Question: {question}
Context: {context}
Answer:

"""
prompt = ChatPromptTemplate.from_template(template)

local_model = "preferred-model-here" #Enter your preferred model here
llm = ChatOllama(model=local_model)

rag_chain = (
        {"context": retriever,  "question": RunnablePassthrough()}
        | prompt
        | llm
        | StrOutputParser()
)

while True:
    query = str(input("Enter Question: "))
    print(rag_chain.invoke(query))