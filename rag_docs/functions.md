# Python Functions

## What is a Function?

A function is a reusable block of code that performs a specific task. Instead of writing the same code multiple times, you can place it inside a function and call it whenever needed.

Functions improve:
- Code reusability
- Readability
- Maintainability
- Modularity

# Creating a Function

Functions are created using the `def` keyword.

### Syntax

```python
def function_name(parameters):
    # Function body
    return value
```

### Example

```python
def greet():
    print("Hello, Welcome to Python!")
```

# Calling a Function

A function does not execute until it is called.

```python
def greet():
    print("Hello!")

greet()
```

Output

```
Hello!
```

---

# Parameters vs Arguments

Many beginners confuse these terms.

### Parameter

A parameter is the variable declared inside the function definition.

```python
def greet(name):
    print(name)
```

Here,

```
name
```

is the parameter.

### Argument

An argument is the actual value passed while calling the function.

```python
greet("Alice")
```

Here,

```
"Alice"
```

is the argument.

---

# Number of Arguments

Python requires the correct number of arguments.

Correct

```python
def add(a, b):
    print(a + b)

add(5, 10)
```

Incorrect

```python
add(5)
```

Output

```
TypeError
```

---

# Return Statement

The `return` statement sends a value back to the caller.

```python
def square(x):
    return x * x

result = square(5)

print(result)
```

Output

```
25
```

If no return statement exists, Python automatically returns `None`.

```python
def hello():
    print("Hi")

print(hello())
```

Output

```
Hi
None
```

---

# Types of Functions

### Function without Parameters

```python
def hello():
    print("Hello")
```

---

### Function with Parameters

```python
def greet(name):
    print("Hello", name)
```

---

### Function with Return Value

```python
def add(a, b):
    return a + b
```

---

### Function without Return Value

```python
def display():
    print("Python")
```

---

# Default Parameters

A parameter can have a default value.

```python
def greet(name="Guest"):
    print("Hello", name)

greet()
greet("Alice")
```

Output

```
Hello Guest
Hello Alice
```

---

# Keyword Arguments

Arguments can be passed using parameter names.

```python
def student(name, age):
    print(name, age)

student(age=20, name="Alice")
```

The order does not matter.

# Positional Arguments

Arguments are matched according to their position.

```python
def student(name, age):
    print(name, age)

student("Alice",20)
```

---

# Arbitrary Arguments (*args)

If the number of arguments is unknown, use `*args`.

Python stores them inside a tuple.

```python
def numbers(*args):
    print(args)

numbers(1,2,3,4)
```

Output

```
(1,2,3,4)
```

Example

```python
def total(*numbers):
    print(sum(numbers))

total(10,20,30)
```

---

# Arbitrary Keyword Arguments (**kwargs)

Unknown keyword arguments are stored inside a dictionary.

```python
def student(**details):
    print(details)

student(name="Alice", age=22)
```

Output

```
{'name':'Alice','age':22}
```

Example

```python
def info(**person):
    print(person["name"])

info(name="John", city="Hyderabad")
```

---

# Passing Lists as Arguments

Lists can be passed directly to functions.

```python
def display(items):
    for item in items:
        print(item)

fruits=["Apple","Banana","Mango"]

display(fruits)
```

---

# Local Variables

Variables created inside a function exist only inside that function.

```python
def test():
    x=10
    print(x)

test()
```

Trying to access `x` outside the function results in an error.

---

# Global Variables

Variables defined outside functions are global.

```python
name="Python"

def show():
    print(name)

show()
```

Output

```
Python
```

---

# The pass Statement

If a function has no implementation yet, use `pass`.

```python
def future_function():
    pass
```

---

# Recursion

Recursion is when a function calls itself.

Example

```python
def factorial(n):

    if n==1:
        return 1

    return n*factorial(n-1)

print(factorial(5))
```

Output

```
120
```

Recursion is useful for

- Tree Traversal
- Divide and Conquer Algorithms
- Dynamic Programming
- Mathematical Problems

---

# Lambda Functions

Lambda functions are anonymous functions.

Syntax

```python
lambda arguments : expression
```

Example

```python
square=lambda x:x*x

print(square(5))
```

Output

```
25
```

Example

```python
add=lambda a,b:a+b

print(add(10,20))
```

Output

```
30
```

---

# Function Scope

Python follows LEGB scope.

- Local
- Enclosing
- Global
- Built-in

Python searches variables in this order.

---

# Docstrings

A docstring explains what a function does.

```python
def add(a,b):
    """
    Returns the sum of two numbers.
    """
    return a+b
```

Access using

```python
print(add.__doc__)
```

---

# Function Annotations

Annotations provide type hints.

```python
def add(a:int,b:int)->int:
    return a+b
```

They improve readability and editor support but are not enforced by Python.


# Special Parameters

Python supports three kinds of parameters.

### Positional-only

```python
def display(name,/):
    print(name)
```
### Keyword-only

```python
def display(*,name):
    print(name)
```
### Positional or Keyword

```python
def display(name):
    print(name)
```
# Unpacking Arguments

Tuple/List unpacking

```python
numbers=[10,20]

def add(a,b):
    print(a+b)

add(*numbers)
```

Dictionary unpacking

```python
student={
"name":"Alice",
"age":22
}

def info(name,age):
    print(name,age)

info(**student)
```

# Best Practices

- Keep functions small.
- Give meaningful names.
- Use return instead of print whenever possible.
- Avoid global variables.
- Write docstrings.
- Use default parameters carefully.
- Use recursion only when necessary.
- Follow PEP 8 naming conventions.

# Common Beginner Mistakes

- Forgetting parentheses while calling a function.
- Missing return statement.
- Incorrect indentation.
- Passing wrong number of arguments.
- Confusing parameters and arguments.
- Returning print() instead of a value.
- Using mutable default arguments like lists.
# Interview Questions

1. What is a function in Python?
2. Why do we use functions?
3. Difference between parameter and argument.
4. Difference between print() and return.
5. What are default arguments?
6. Explain *args and **kwargs.
7. What is recursion?
8. What are lambda functions?
9. What is function scope?
10. What are local and global variables?
11. What are positional and keyword arguments?
12. What is a docstring?
13. What are function annotations?
14. What is argument unpacking?
15. What happens if a function has no return statement?

# Summary

Functions are reusable blocks of code that improve modularity and readability. Python supports positional arguments, keyword arguments, default parameters, arbitrary arguments (`*args`), arbitrary keyword arguments (`**kwargs`), recursion, lambda expressions, type annotations, and docstrings, making functions flexible and powerful for building reusable applications.