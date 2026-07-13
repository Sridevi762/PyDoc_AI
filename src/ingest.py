"""
ingest.py
-------------------------
Loads all markdown documents from the rag_docs folder.
"""

from pathlib import Path

from config import RAG_DOCS_PATH


def load_documents():
    """
    Reads every .md file inside rag_docs folder.

    Returns:
        List[dict]
    """

    documents = []

    if not RAG_DOCS_PATH.exists():
        print("❌ rag_docs folder not found.")
        return documents

    markdown_files = list(RAG_DOCS_PATH.rglob("*.md"))

    if not markdown_files:
        print("❌ No markdown files found.")
        return documents

    for file in markdown_files:
        try:
            content = file.read_text(
                encoding="utf-8",
                errors="ignore"
            )

            documents.append(
                {
                    "filename": file.name,
                    "filepath": str(file),
                    "content": content
                }
            )

        except Exception as e:
            print(f"❌ Failed to read {file.name}")
            print(e)

    return documents


def print_summary(documents):
    """
    Prints a summary of loaded documents.
    """

    print("\n========== DOCUMENT SUMMARY ==========\n")

    print(f"Total Documents : {len(documents)}\n")

    for doc in documents:

        print(f"📄 {doc['filename']}")
        print(f"Characters : {len(doc['content'])}")
        print("-" * 50)


if __name__ == "__main__":

    docs = load_documents()

    print_summary(docs)