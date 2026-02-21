import os
from langchain_community.document_loaders import PyPDFLoader, TextLoader, Docx2txtLoader

SUPPORTED_EXTENSIONS = [".pdf", ".txt", ".docx"]

def load_documents(folder_path: str):
    documents = []

    for file in os.listdir(folder_path):
        path = os.path.join(folder_path, file)
        ext = os.path.splitext(file)[1].lower()

        if ext not in SUPPORTED_EXTENSIONS:
            continue

        if ext == ".pdf":
            loader = PyPDFLoader(path)
        elif ext == ".txt":
            loader = TextLoader(path, encoding="utf-8")
        elif ext == ".docx":
            loader = Docx2txtLoader(path)

        documents.extend(loader.load())

    return documents
