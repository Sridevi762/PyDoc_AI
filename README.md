# 🐍 PyDoc AI

## Problem Statement

Learning Python programming often requires searching through multiple documentation pages, tutorials, and error solutions. Beginners and developers may find it difficult to quickly understand Python concepts, syntax, and common errors.

The goal of PyDoc AI is to provide an AI-powered assistant that helps users get quick and accurate answers to Python-related questions by using a Python knowledge base and Retrieval Augmented Generation (RAG).

## 📌 Project Overview
how to check my readme satisfies all the project rules

To check whether your README.md satisfies all project rules, you need to compare it against your K-Hub Batch 2026-27 project requirements (AI chatbot + documentation + RAG requirements). Use this checklist.

1. Check README structure

Open your README.md and verify it has these sections:

# Project Title

## Overview

## Problem Statement

## Features

## Tech Stack

## Project Architecture

## Folder Structure

## How It Works

## Installation

## Usage

## RAG Implementation

## Knowledge Base

## Example Queries

## Limitations

## Future Improvements

## Contributors

If important sections are missing, add them.

2. Project description check

Your README should clearly explain:

✅ What is the project?

Example:

PyDoc AI is an AI-powered Python Documentation Assistant that answers Python programming questions using Retrieval Augmented Generation (RAG).

Check that it mentions:

Domain: Python Programming
AI chatbot
Documentation assistant
RAG (if implemented)
Knowledge base
3. Rule: Domain-specific chatbot

Your README should prove that your chatbot is domain-specific.

Check for:

✅ It answers only Python questions.

Example:

Supported:
- Python syntax
- Data types
- Functions
- OOP concepts
- Exception handling
- Common Python errors

Not supported:
- General conversation
- Non-Python programming languages
4. Rule: RAG implementation

Your README should explain your RAG pipeline.

It should contain something like:

User Question
       |
       ↓
Query Embedding
       |
       ↓
Vector Database Search
       |
       ↓
Relevant Python Documentation Chunks
       |
       ↓
LLM Response Generation
       |
       ↓
Final Answer

Also mention:

Document collection
Chunking
Embeddings
Vector store
Retrieval
Answer generation
5. Rule: Knowledge source

Check that you mention your sources.

Example:

Knowledge Base Sources:

1. Python Official Documentation
   https://docs.python.org/

2. Python Tutorial
   https://docs.python.org/3/tutorial/

3. W3Schools Python Reference
6. Rule: Installation instructions

Someone else should be able to run your project.

Check:

Requirements

Example:

Python 3.10+

Libraries:
- streamlit
- sentence-transformers
- chromadb
- ollama
Installation

Example:

git clone <repository-url>

cd PyDoc_AI

pip install -r requirements.txt
7. Rule: Usage instructions

Your README should show:

streamlit run app.py

and example questions:

User:
What is a Python list?

AI:
A list is a mutable collection...
8. Rule: Folder structure

Your README should match your actual project.

Example:

PyDoc_AI/

│── app.py
│── chatbot.py
│── rag.py
│── embeddings.py
│── prompt.py
│── config.py
│── requirements.txt

│── knowledge_base/
│    ├── python_basics.md
│    ├── functions.md
│    ├── oops.md
│    └── exceptions.md

│── vector_store/

│── README.md

Make sure names exactly match your files.

9. Rule: Screenshots/demo

Many project evaluations expect proof.

Add:

## Screenshots

1. Chat interface
2. Python question answer
3. Error explanation example
10. Check GitHub readiness

Before submission:

Run:

git status

Make sure:

❌ Not uploaded:

.env
venv/
__pycache__/
vector database files
large model files

Your .gitignore should contain:

venv/
.env
__pycache__/
*.pyc
vector_store/
11. Final README self-test

Ask yourself:

Requirement	Present?
Project title	✅/❌
Problem explanation	✅/❌
AI chatbot mentioned	✅/❌
Domain restriction explained	✅/❌
RAG workflow explained	✅/❌
Knowledge sources listed	✅/❌
Installation steps	✅/❌
Run command	✅/❌
Folder structure	✅/❌
Screenshots	✅/❌
Future improvements	✅/❌

If you paste your current README.md here, I can review it against the K-Hub project rules and tell you exactly what is missing or needs modification.

## How It Works

1. User asks a Python question.
2. The retriever searches the knowledge base.
3. Relevant documents are retrieved.
4. Context is added to the prompt.
5. Llama 3.2 generates the response.
6. The chatbot displays the answer.but if the relevant information is not in rag files then it will give on its own 

Yes, that is an important point. Your current "How It Works" section suggests that the chatbot only answers from the RAG knowledge base, but your actual behavior is different: if the information is not found in the retrieved documents, the Llama model can still generate an answer from its own pre-trained knowledge.

You should update your README to describe this accurately.

Use something like:

## How It Works

1. User asks a Python-related question.
2. The retriever searches the Python knowledge base for relevant documents.
3. Relevant document chunks are retrieved and added as context.
4. The context and user query are passed to the Llama 3.2 model.
5. If relevant information is available in the knowledge base, the model uses the retrieved context to generate a grounded response.
6. If the required information is not available in the knowledge base, the model can use its pre-trained knowledge to answer the Python question.
7. The chatbot displays the final response to the user.

Also, add a note under Limitations or RAG Implementation:

## RAG Behavior

PyDoc AI uses Retrieval Augmented Generation (RAG) to improve answer accuracy by providing relevant Python documentation context to the LLM. However, when a query does not match the available knowledge base documents, the Llama 3.2 model may generate responses using its internal knowledge.

One more thing: if your project rule says "answer only from provided documents", then this behavior may violate the requirement. In that case, you need to add a confidence check in your RAG pipeline and return:

"I couldn't find this information in my Python documentation."

instead of allowing Llama to answer freely.

For your current PyDoc AI project, decide based on the evaluation rule:

General Python assistant → current behavior is acceptable.
Strict documentation assistant → restrict answers to RAG context only.
Problem explanation	✅/❌
AI chatbot mentioned	✅/❌
Domain restriction explained give me matter for this 

For your PyDoc AI (Python Documentation Assistant) README, you can add the following content.

Problem Explanation
## Problem Statement

Learning Python programming often requires searching through multiple documentation pages, tutorials, and error solutions. Beginners and developers may find it difficult to quickly understand Python concepts, syntax, and common errors.
The goal of PyDoc AI is to provide an AI-powered assistant that helps users get quick and accurate answers to Python-related questions by using a Python knowledge base and Retrieval Augmented Generation (RAG).


## Overview

PyDoc AI is an AI-powered Python Documentation Assistant chatbot designed to help users learn and troubleshoot Python programming concepts.
The chatbot uses Large Language Models (LLM) with Retrieval Augmented Generation (RAG) to retrieve relevant information from Python documentation and generate helpful responses.

PyDoc AI helps users learn Python programming by answering questions related to:

- Python Basics
- Data Types
- Operators
- Control Flow
- Functions
- Object-Oriented Programming
- File Handling
- Exception Handling
- Modules
- Common Errors
- Best Practices

The chatbot retrieves relevant information from a Python knowledge base before generating responses, improving accuracy and ensuring domain-specific answers.

## 🚀 Features

- User Registration & Login
- Interactive Chat Interface
- Retrieval-Augmented Generation (RAG)
- Local Llama 3.2 Model using Ollama
- Python Documentation Knowledge Base
- Chat History Storage
- Delete Individual Chats
- Start New Chat
- Domain-Specific Responses
- Suggested Questions
- Modern Streamlit UI

## 🛠 Tech Stack

**Frontend**
- Streamlit

**Backend**
- Python

**AI Model**
- Llama 3.2 (Ollama)

**Vector Database**
- ChromaDB

**Embeddings**
- Sentence Transformers

**Database**
- SQLite

**Libraries**
- LangChain
- Streamlit
- ChromaDB
- Sentence Transformers
- Ollama
- SQLite3

## 📂 Project Structure

```text
PyDoc_AI/
│
├── app.py
├── auth.py
├── database.py
├── chat_history.py
├── evaluation.py
├── build_vector_db.py
├── requirements.txt
├── README.md
├── users.db
│
├── rag_docs/
│   ├── python_basics.md
│   ├── data_types.md
│   ├── operators.md
│   ├── control_flow.md
│   ├── functions.md
│   ├── oops.md
│   ├── file_handling.md
│   ├── exception_handling.md
│   ├── modules.md
│   ├── common_errors.md
│   └── best_practices.md
│
├── chroma_db/
│
└── src/
    ├── __init__.py
    ├── chatbot.py
    ├── config.py
    ├── document_loader.py
    ├── embeddings.py
    ├── ingest.py
    ├── llm.py
    ├── prompts.py
    ├── rag.py
    ├── rag_pipeline.py
    ├── retriever.py
    ├── text_splitter.py
    └── vector_store.py
    
```

## ⚙ Installation

Clone the repository

```bash
git clone https://github.com/yourusername/PyDoc-AI.git
```

Move into the project folder

```bash
cd PyDoc-AI
```

Create a virtual environment

```bash
python -m venv venv
```

Activate the environment

Windows

```bash
venv\Scripts\activate
```

Linux / Mac

```bash
source venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

## Install Ollama

Download and install Ollama.

Pull the Llama model.

```bash
ollama pull llama3.2
```

Run the model.

```bash
ollama run llama3.2
```

## Create Embeddings

```bash
python embeddings.py
```

This creates the vector database from the Python documentation.

## Run the Application

```bash
streamlit run app.py
```

## How It Works

1. User asks a Python-related question.
2. The retriever searches the Python knowledge base for relevant documents.
3. Relevant document chunks are retrieved and added as context.
4. The context and user query are passed to the Llama 3.2 model.
5. If relevant information is available in the knowledge base, the model uses the retrieved context to generate a grounded response.
6. If the required information is not available in the knowledge base, the model can use its pre-trained knowledge to answer the Python question.
7. The chatbot displays the final response to the user.

## Screenshots

### Chat Interface

![PyDoc AI Chat Interface](assets/chat_interface.png)

### Python Question Answering

![Python Answer Example](assets/python_answer.png)

## Knowledge Base

The chatbot uses Markdown documentation covering:

- Python Basics
- Data Types
- Operators
- Control Flow
- Functions
- OOP
- Modules
- File Handling
- Exception Handling
- Common Errors
- Best Practices

## Evaluation

The chatbot was tested using multiple Python programming questions, including:

- What is Python?
- Explain loops.
- What is inheritance?
- Explain exception handling.
- Difference between list and tuple.
- Explain decorators.
- Explain file handling.

The chatbot successfully answered domain-specific questions using the RAG pipeline.

## Why RAG Instead of Fine-Tuning?

This project uses Retrieval-Augmented Generation (RAG) instead of fine-tuning because it:

- Retrieves relevant documentation before answering.
- Produces accurate, domain-specific responses.
- Reduces hallucinations.
- Does not require expensive model training.
- Is lightweight and efficient for local deployment.

## Trade-off

Using RAG provides accurate responses without expensive fine-tuning. However, response quality depends on the quality and completeness of the knowledge base.

## Future Improvements

- Source Citations
- Automatic Knowledge Base Updates using Web Scraping
- Voice Assistant
- Dark Mode
- Code Execution Support

