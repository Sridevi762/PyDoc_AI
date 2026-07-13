# from src.retriever import Retriever


# class RAGPipeline:
#     """
#     Handles Retrieval Augmented Generation workflow.
#     """


#     def __init__(self):

#         self.retriever = Retriever()



#     def get_context(self, query):
#         """
#         Retrieves relevant documents
#         and prepares context for LLM.
#         """

#         documents = self.retriever.retrieve(
#             query
#         )


#         context = ""


#         for doc in documents:

#             context += (
#                 "\n\n"
#                 + doc["content"]
#             )


#         return context

from src.retriever import Retriever


class RAGPipeline:
    """
    Handles Retrieval Augmented Generation workflow.
    """


    def __init__(self):

        self.retriever = Retriever()



    def get_context(self, query):
        """
        Retrieves relevant documents
        and prepares context for LLM.
        """


        documents = self.retriever.retrieve(
            query
        )


        # No relevant documents found
        if not documents:

            return (
                "No relevant information was found. "
                "Answer using your Python knowledge."
            )


        context = ""


        for doc in documents:

            context += (
                "\n\n"
                + doc["content"]
            )


        return context