from src.chatbot import PyDocAI

bot = PyDocAI()

test_questions = [
    "What is Python?",
    "Explain loops in Python.",
    "What is inheritance?",
    "Explain exception handling.",
    "How do you open a file in Python?",
    "What is a list comprehension?",
    "What is the difference between list and tuple?",
    "Explain decorators.",
    "What is a lambda function?",
    "How do try and except work?"
]

print("=" * 70)
print("PyDoc AI Evaluation")
print("=" * 70)

for i, question in enumerate(test_questions, start=1):

    print(f"\nQuestion {i}: {question}")

    answer = bot.ask(question)

    print("\nAnswer:")
    print(answer)

    print("-" * 70)