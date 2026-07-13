# import ollama

# from src.config import MODEL_NAME


# class LLM:

#     """
#     Handles communication with local Ollama LLM.
#     """


#     def __init__(self):

#         self.model = MODEL_NAME



#     def generate(
#         self,
#         prompt
#     ):
#         """
#         Sends prompt to Ollama
#         and returns generated response.
#         """


#         response = ollama.chat(

#             model=self.model,

#             messages=[
#                 {
#                     "role": "user",
#                     "content": prompt
#                 }
#             ]

#         )


#         return response["message"]["content"]

import ollama

from src.config import MODEL_NAME


class LLM:
    """
    Handles communication with local Ollama LLM.
    """

    def __init__(self):

        self.model = MODEL_NAME


    def generate(self, prompt):
        """
        Sends prompt to Ollama
        and returns generated response.
        """

        response = ollama.chat(

            model=self.model,

            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],

            options={

                "temperature": 0.2,

                "num_predict": 150,

                "top_p": 0.8,

                "repeat_penalty": 1.1,

                "num_ctx": 2048

            }

        )

        answer = response["message"]["content"].strip()

        return answer