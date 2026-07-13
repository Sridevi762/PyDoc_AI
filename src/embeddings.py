from sentence_transformers import SentenceTransformer


class EmbeddingModel:
    """
    Creates embeddings from text chunks
    using a local sentence transformer model.
    """


    def __init__(self):

        self.model = SentenceTransformer(
            "all-MiniLM-L6-v2"
        )


    def generate_embeddings(self, texts):
        """
        Converts a list of texts into vectors.

        Args:
            texts:
                List of strings

        Returns:
            Embedding vectors
        """


        embeddings = self.model.encode(
            texts,
            convert_to_numpy=True
        )


        return embeddings