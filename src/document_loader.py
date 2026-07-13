import os


class DocumentLoader:
    """
    Loads documents from the RAG knowledge base.
    Supports markdown and text files.
    """


    def __init__(self, folder_path):
        self.folder_path = folder_path


    def load_documents(self):
        """
        Reads all supported files from the knowledge base folder.

        Returns:
            List of dictionaries containing:
            - source: document name
            - content: document text
        """

        documents = []


        for filename in os.listdir(self.folder_path):

            file_path = os.path.join(
                self.folder_path,
                filename
            )


            # Support markdown and text documents
            if filename.endswith(
                (".md", ".txt")
            ):

                with open(
                    file_path,
                    "r",
                    encoding="utf-8"
                ) as file:

                    content = file.read()


                documents.append(
                    {
                        "source": filename,
                        "content": content
                    }
                )


        return documents