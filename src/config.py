import os


BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)


RAG_DOCS_PATH = os.path.join(
    BASE_DIR,
    "rag_docs"
)


CHROMA_DB_PATH = os.path.join(
    BASE_DIR,
    "chroma_db"
)


MODEL_NAME = "llama3.2"


TOP_K = 3