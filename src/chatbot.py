from src.rag_pipeline import RAGPipeline
from src.llm import LLM
from src.prompts import SYSTEM_PROMPT


class PyDocAI:

    def __init__(self):

        self.rag = RAGPipeline()
        self.llm = LLM()

    # -----------------------------------
    # Detect Python Questions / Code
    # -----------------------------------

    def is_python_question(self, question):

        question = question.lower().strip()

        python_keywords = [

            # General
            "python",
            "code",
            "program",
            "script",
            "syntax",

            # Data Types
            "list",
            "tuple",
            "dictionary",
            "dict",
            "set",
            "string",
            "int",
            "float",
            "bool",

            # Concepts
            "variable",
            "operator",
            "function",
            "class",
            "object",
            "inheritance",
            "polymorphism",
            "encapsulation",
            "abstraction",

            # Loops & Conditions
            "loop",
            "for",
            "while",
            "if",
            "elif",
            "else",

            # Modules
            "module",
            "package",
            "import",
            "pip",

            # Errors
            "error",
            "errors",
            "bug",
            "debug",
            "exception",
            "traceback",

            "typeerror",
            "nameerror",
            "valueerror",
            "indexerror",
            "keyerror",
            "attributeerror",
            "syntaxerror",
            "indentationerror",
            "importerror",
            "modulenotfounderror",
            "zerodivisionerror",

            # Advanced
            "lambda",
            "decorator",
            "generator",
            "iterator",
            "pep8",
            "file handling",
            "exception handling"
        ]

        if any(keyword in question for keyword in python_keywords):
            return True

        # Detect Python code snippets

        code_patterns = [

            "print(",
            "def ",
            "class ",
            "import ",
            "from ",
            "return ",
            "try:",
            "except",
            "finally:",
            "raise ",
            "with ",
            "pass",
            "break",
            "continue",

            "=",
            "[",
            "]",
            "{",
            "}",
            "(",
            ")",
            ":"
        ]

        if any(pattern in question for pattern in code_patterns):
            return True

        return False

    # -----------------------------------
    # Decide when to use RAG
    # -----------------------------------

    def needs_rag(self, question):

        rag_keywords = [

            "best practice",
            "best practices",

            "interview",

            "common error",
            "common errors",

            "faq",

            "coding standard",

            "pep8",

            "file handling",

            "decorator",

            "generator",

            "iterator",

            "exception handling",

            "object oriented",

            "oops",

            "inheritance",

            "polymorphism",

            "encapsulation",

            "difference",

            "compare",

            "explain in detail"
        ]

        question = question.lower()

        return any(
            keyword in question
            for keyword in rag_keywords
        )

    # -----------------------------------
    # Skip RAG for very simple questions
    # -----------------------------------

    def is_simple_question(self, question):

        simple_questions = [

            "what is python",

            "what are functions",

            "what is a list",

            "what is tuple",

            "what is dictionary",

            "what is oop",

            "what are loops"
        ]

        question = question.lower()

        return any(
            q in question
            for q in simple_questions
        )

    # -----------------------------------
    # Main Chat Function
    # -----------------------------------

    def ask(self, question):

        # Reject non-Python questions

        if not self.is_python_question(question):

            return (
                "I can help only with Python-related questions.\n\n"
                "Please ask me about Python programming, coding, debugging, or Python errors."
            )

        context = ""

        if self.needs_rag(question):

            context = self.rag.get_context(question)

        elif self.is_simple_question(question):

            context = ""

        prompt = SYSTEM_PROMPT.format(

            context=context,
            question=question

        )

        return self.llm.generate(prompt)