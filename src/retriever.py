from src.vector_store import VectorStore
from src.config import TOP_K


class Retriever:
    """
    Retrieves relevant document chunks
    from the ChromaDB vector database.
    """


    def __init__(self):

        self.vector_store = VectorStore()

        # Load existing ChromaDB database
        self.vector_store.load()



    def retrieve(self, query):
        """
        Retrieves relevant chunks for a query.
        """


        results = self.vector_store.search(
            query,
            TOP_K
        )


        # If no relevant results found
        if not results:

            return []


        return results