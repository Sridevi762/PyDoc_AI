# Python Basics

## What is Python?

Python is a high-level, interpreted, general-purpose programming language created by **Guido van Rossum** and first released in **1991**. It emphasizes code readability through a clean and simple syntax, making it one of the easiest programming languages to learn.

Python supports multiple programming paradigms, including procedural, object-oriented, and functional programming. Due to its extensive standard library and active community, Python is widely used by beginners, researchers, software developers, and large organizations.

---

# History of Python

Python was developed by **Guido van Rossum** in the late 1980s and officially released in 1991.

The language was inspired by the ABC programming language and was designed to overcome its limitations while maintaining simplicity and readability.

Python continues to evolve through Python Enhancement Proposals (PEPs), with Python 3 being the current major version.

---

# Why Python is Popular

Python is popular because it allows developers to write programs with fewer lines of code compared to many other programming languages.

Reasons for its popularity include:

- Easy to learn
- Clean and readable syntax
- Huge standard library
- Large developer community
- Cross-platform compatibility
- Open-source
- Extensive third-party libraries
- Used in modern technologies such as AI, Machine Learning, and Data Science

---

# Features of Python

Python provides several features that make it a preferred programming language.

- High-level programming language
- Interpreted language
- Dynamically typed
- Object-oriented
- Platform independent
- Automatic memory management
- Large standard library
- Supports multiple programming paradigms
- Open-source and free
- Extensible and embeddable

---

# Applications of Python

Python is widely used in various domains.

- Web Development
- Data Analysis
- Data Science
- Machine Learning
- Artificial Intelligence
- Automation
- Cybersecurity
- Cloud Computing
- Desktop Applications
- Web Scraping
- Scientific Computing
- Internet of Things (IoT)
- Game Development

---

# Advantages of Python

- Easy to learn
- Readable syntax
- Large collection of libraries
- Faster application development
- Cross-platform support
- Strong community support
- Suitable for rapid prototyping

---

# Limitations of Python

Although Python is powerful, it has some limitations.

- Slower execution compared to C and C++
- Higher memory consumption
- Not commonly used for mobile application development
- Global Interpreter Lock (GIL) limits true multithreading

---

# Installing Python

Steps to install Python:

1. Download Python from the official website.
2. Run the installer.
3. Select **Add Python to PATH**.
4. Click **Install Now**.
5. Verify the installation.

```bash
python --version
```

Example Output

```
Python 3.13.7
```

---

# Python Interpreter vs Script Mode

## Interpreter Mode

Interpreter mode executes one statement at a time.

Example

```python
>>> print("Hello")
```

Output

```
Hello
```

---

## Script Mode

Script mode executes an entire Python file.

Example

```bash
python app.py
```

---

# First Python Program

```python
print("Hello, World!")
```

Output

```
Hello, World!
```

---

# Python Syntax

Python uses indentation instead of curly braces to define code blocks.

Example

```python
age = 18

if age >= 18:
    print("Eligible to vote")
```

---

# Variables

Variables are used to store values in memory.

Example

```python
name = "Alice"
age = 22
height = 5.8
is_student = True
```

Python automatically determines the variable type.

---

# Variable Naming Rules

Rules for naming variables:

- Can contain letters, digits, and underscores
- Cannot start with a digit
- Cannot contain spaces
- Cannot use Python keywords
- Variable names are case-sensitive

Correct

```python
student_name = "John"
marks1 = 95
```

Incorrect

```python
1student = "John"
class = "Python"
```

---

# Comments

Comments improve code readability.

Single-line comment

```python
# This is a comment
```

Multi-line comment

```python
"""
This is a
multi-line comment
"""
```

---

# Input and Output

Input

```python
name = input("Enter your name: ")
```

Output

```python
print("Welcome", name)
```

---

# Dynamic Typing

Python is dynamically typed.

Example

```python
x = 10
print(type(x))

x = "Python"
print(type(x))
```

Output

```
<class 'int'>
<class 'str'>
```

---

# Type Conversion

Python allows explicit type conversion.

```python
age = "20"

print(int(age))
```

```python
price = 100

print(float(price))
```

Output

```
20
100.0
```

---

# Case Sensitivity

Python is case-sensitive.

```python
name = "Alice"
Name = "Bob"

print(name)
print(Name)
```

Output

```
Alice
Bob
```

---

# Multiple Assignment

Python allows assigning multiple values.

```python
a = b = c = 10

x, y, z = 1, 2, 3
```

---

# Keywords

Keywords are reserved words with predefined meanings.

Examples

```
if
else
for
while
def
class
return
import
try
except
True
False
None
```

---

# Basic Operators

## Arithmetic Operators

```python
+
-
*
/
%
//
**
```

## Comparison Operators

```python
==
!=
>
<
>=
<=
```

## Logical Operators

```python
and
or
not
```

---

# Indentation

Python uses indentation to define blocks.

Correct

```python
if 5 > 2:
    print("True")
```

Incorrect

```python
if 5 > 2:
print("True")
```

This raises an **IndentationError**.

---

# Common Beginner Mistakes

- Forgetting indentation
- Misspelling variable names
- Using keywords as variable names
- Missing quotation marks
- Mixing tabs and spaces
- Confusing `=` with `==`
- Forgetting parentheses in function calls

---

# Best Practices

- Use meaningful variable names.
- Follow PEP 8 coding style.
- Write reusable code.
- Keep functions small.
- Add comments only where necessary.
- Use consistent indentation.
- Use descriptive function names.

---

# Frequently Asked Questions

### Is Python compiled or interpreted?

Python is primarily an interpreted language.

---

### Is Python case-sensitive?

Yes.

---

### Is Python free?

Yes. Python is free and open-source.

---

### Can Python build websites?

Yes. Frameworks like Django and Flask are widely used.

---

### Why is Python popular?

Because it is simple, readable, and has thousands of useful libraries.

---

### Does Python support Object-Oriented Programming?

Yes.

---

### Can Python be used for Artificial Intelligence?

Yes. Libraries such as TensorFlow, PyTorch, and Scikit-learn are commonly used.

---

# Interview Questions

1. What is Python?
2. Who created Python?
3. Why is Python called an interpreted language?
4. What are the main features of Python?
5. Explain dynamic typing.
6. Explain indentation.
7. Difference between `=` and `==`.
8. What are Python keywords?
9. What are the advantages of Python?
10. What are the limitations of Python?
11. Explain case sensitivity.
12. What is type conversion?
13. Difference between Interpreter Mode and Script Mode?
14. Why is Python popular for AI and Data Science?
15. Name some real-world applications of Python.

---

# Summary

Python is a powerful, high-level, interpreted programming language designed for readability and simplicity. It is widely used in web development, automation, data science, machine learning, artificial intelligence, cloud computing, and many other domains. Its clean syntax, extensive libraries, and active community make it one of the most popular programming languages in the world.
