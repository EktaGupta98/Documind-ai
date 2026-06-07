import os

from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

from src.document_loader import load_documents


DATA_PATH = "data"
DB_FAISS_PATH = "vector_store/db_faiss"


def create_vectorstore():

    documents = load_documents(DATA_PATH)

    if len(documents) == 0:
        raise Exception(
            "No documents found in data folder."
        )

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )

    chunks = splitter.split_documents(documents)

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    db = FAISS.from_documents(
        chunks,
        embeddings
    )

    os.makedirs(
        DB_FAISS_PATH,
        exist_ok=True
    )

    db.save_local(
        DB_FAISS_PATH
    )

    print(
        f"Vectorstore created successfully with {len(chunks)} chunks."
    )


if __name__ == "__main__":

    create_vectorstore()