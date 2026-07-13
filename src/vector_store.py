from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings

from src.config import CHROMA_DB_PATH

from functools import lru_cache
@lru_cache(maxsize=1)
def get_embedding_model():

    return HuggingFaceEmbeddings(
        model_name="all-MiniLM-L6-v2"
    )


class VectorStore:

    def __init__(self):

        self.embedding_model = get_embedding_model()

        self.vector_db = None

    def create_store(self, chunks):

        texts = [
            chunk["content"]
            for chunk in chunks
        ]


        metadatas = [
            {
                "source": chunk["source"]
            }
            for chunk in chunks
        ]


        self.vector_db = Chroma.from_texts(
            texts=texts,
            embedding=self.embedding_model,
            metadatas=metadatas,
            persist_directory=CHROMA_DB_PATH
        )



    def load(self):

        self.vector_db = Chroma(
            persist_directory=CHROMA_DB_PATH,
            embedding_function=self.embedding_model
        )



    def search(
        self,
        query,
        top_k=5
    ):

        results = self.vector_db.similarity_search_with_score(
            query,
            k=top_k
        )


        documents = []


        for result, score in results:

            # Lower score means better similarity in Chroma
            if score < 1.0:

                documents.append(
                    {
                        "content": result.page_content,
                        "source": result.metadata["source"]
                    }
                )


        return documents