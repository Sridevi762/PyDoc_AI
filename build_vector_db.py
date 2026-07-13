from src.config import RAG_DOCS_PATH
from src.document_loader import DocumentLoader
from src.text_splitter import TextSplitter
from src.vector_store import VectorStore


def build_database():

    print("Loading documents...")

    loader = DocumentLoader(
        RAG_DOCS_PATH
    )

    documents = loader.load_documents()

    print(
        f"Loaded {len(documents)} documents"
    )


    print("Splitting documents...")

    splitter = TextSplitter()

    chunks = splitter.split_documents(
        documents
    )

    print(
        f"Created {len(chunks)} chunks"
    )


    print("Building ChromaDB database...")

    vector_store = VectorStore()


    vector_store.create_store(
        chunks
    )


    print(
        "ChromaDB created successfully!"
    )


if __name__ == "__main__":

    build_database()