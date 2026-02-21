import os

from langchain_community.vectorstores import FAISS
from langchain_community.embeddings.cohere import CohereEmbeddings


def create_vectorstore(chunks):
    cohere_api_key = os.getenv("COHERE_API_KEY")
    if not cohere_api_key:
        raise ValueError("COHERE_API_KEY is not set.")

    embed_model = os.getenv("COHERE_EMBED_MODEL", "embed-english-v3.0")
    embeddings = CohereEmbeddings(
        cohere_api_key=cohere_api_key,
        model=embed_model,
    )
    return FAISS.from_documents(chunks, embeddings)
