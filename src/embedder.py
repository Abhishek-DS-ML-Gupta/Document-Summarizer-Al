from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
import os


def create_vector_store(chunks, store_path="data/vector_store/index"):
    embeddings = OpenAIEmbeddings()
    vectorstore = FAISS.from_texts(chunks, embeddings)
    vectorstore.save_local(store_path)
    return vectorstore

def load_vector_store(store_path="data/vector_store/index"):
    embeddings = OpenAIEmbeddings()
    return FAISS.load_local(store_path, embeddings, allow_dangerous_deserialization=True)
