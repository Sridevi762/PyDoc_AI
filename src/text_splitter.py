from langchain_text_splitters import RecursiveCharacterTextSplitter


class TextSplitter:
    """
    Splits documents into smaller chunks
    for embedding and retrieval.
    """


    def __init__(
        self,
        chunk_size=800,
        chunk_overlap=150
    ):

        self.splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap,
            separators=[
                "\n\n",
                "\n",
                " ",
                ""
            ]
        )


    def split_documents(self, documents):
        """
        Splits loaded documents into chunks.

        Input:
            documents:
            [
              {
                source: filename,
                content: text
              }
            ]

        Output:
            List of chunks with metadata
        """


        chunks = []


        for document in documents:

            split_texts = self.splitter.split_text(
                document["content"]
            )


            for text in split_texts:

                chunks.append(
                    {
                        "source": document["source"],
                        "content": text
                    }
                )


        return chunks