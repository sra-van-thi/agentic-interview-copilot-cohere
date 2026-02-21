from rag.document_loader import load_documents
from rag.chunking import chunk_documents
from rag.vectorstore import create_vectorstore

def ingest(folder_path: str):
    docs = load_documents(folder_path)
    chunks = chunk_documents(docs)
    return create_vectorstore(chunks)
