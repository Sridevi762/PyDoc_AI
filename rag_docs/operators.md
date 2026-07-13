# Operators

## What are Operators?

Operators are special symbols or keywords in Python that perform operations on variables, values, or expressions. They allow programmers to manipulate data, perform mathematical calculations, compare values, assign variables, evaluate logical conditions, and perform many other operations.

For example, the addition operator (`+`) adds two numbers, while the comparison operator (`==`) checks whether two values are equal.

Example:

```python
a = 10
b = 20

print(a + b)
```

Output

```
30
```

Without operators, Python programs cannot perform calculations or make decisions.

---

# Why are Operators Important?

Operators are one of the most fundamental concepts in Python programming. Almost every Python program uses operators.

Operators help us to:

- Perform arithmetic calculations.
- Assign values to variables.
- Compare values.
- Make decisions in conditional statements.
- Combine multiple conditions.
- Check whether an item exists in a collection.
- Perform binary operations.

Example:

```python
age = 20

if age >= 18:
    print("Eligible to Vote")
```

Output

```
Eligible to Vote
```

Here, the operator `>=` compares two values.

---

# Types of Operators

Python provides the following built-in operators.

| Operator Category | Purpose |
|-------------------|---------|
| Arithmetic Operators | Perform mathematical operations |
| Assignment Operators | Assign values to variables |
| Comparison Operators | Compare two values |
| Logical Operators | Combine conditional expressions |
| Identity Operators | Compare memory locations |
| Membership Operators | Check whether a value exists in a sequence |
| Bitwise Operators | Perform binary operations |

---

# Arithmetic Operators

## What are Arithmetic Operators?

Arithmetic operators are used to perform common mathematical operations such as addition, subtraction, multiplication, division, finding remainders, powers, and floor division.

Python provides seven arithmetic operators.

---

# Addition Operator (+)

## Definition

The addition operator adds two or more numeric values. When used with strings, it joins (concatenates) them together.

### Syntax

```python
result = operand1 + operand2
```

---

### Example 1

```python
a = 10
b = 25

print(a + b)
```

Output

```
35
```

---

### Example 2

```python
price = 99.50
gst = 18.00

print(price + gst)
```

Output

```
117.5
```

---

### String Concatenation

```python
first_name = "Sri"
last_name = "Durga"

print(first_name + " " + last_name)
```

Output

```
Sri Durga
```

---

### Real-world Example

```python
maths = 90
science = 95
english = 92

total = maths + science + english

print(total)
```

Output

```
277
```

---

### Common Mistake

```python
age = "20"

print(age + 5)
```

Output

```
TypeError
```

Correct way

```python
age = "20"

print(int(age) + 5)
```

Output

```
25
```

---

# Subtraction Operator (-)

## Definition

The subtraction operator subtracts one value from another.

### Syntax

```python
result = operand1 - operand2
```

---

### Example

```python
a = 50
b = 18

print(a - b)
```

Output

```
32
```

---

### Real-world Example

```python
total_marks = 500
obtained = 465

lost_marks = total_marks - obtained

print(lost_marks)
```

Output

```
35
```

---

# Multiplication Operator (*)

## Definition

The multiplication operator multiplies two numbers.

### Syntax

```python
result = operand1 * operand2
```

---

### Example

```python
length = 15
width = 6

print(length * width)
```

Output

```
90
```

---

### String Repetition

The multiplication operator can also repeat strings.

```python
print("Python " * 3)
```

Output

```
Python Python Python
```

---

### Real-world Example

```python
price = 150
quantity = 5

bill = price * quantity

print(bill)
```

Output

```
750
```

---

# Division Operator (/)

## Definition

The division operator divides one number by another.

Unlike floor division, it always returns a floating-point value.

### Syntax

```python
result = operand1 / operand2
```

---

### Example

```python
print(20 / 5)
```

Output

```
4.0
```

---

### Example

```python
print(7 / 2)
```

Output

```
3.5
```

---

### Real-world Example

```python
marks = 450
subjects = 5

average = marks / subjects

print(average)
```

Output

```
90.0
```

---

# Modulus Operator (%)

## Definition

The modulus operator returns the remainder after division.

### Syntax

```python
result = operand1 % operand2
```

---

### Example

```python
print(15 % 4)
```

Output

```
3
```

---

### Checking Even or Odd

```python
number = 18

if number % 2 == 0:
    print("Even")
else:
    print("Odd")
```

Output

```
Even
```

---

### Real-world Uses

The modulus operator is commonly used for:

- Checking even or odd numbers.
- Determining leap years.
- Creating cyclic patterns.
- Finding remainders.

---

# Exponentiation Operator (**)

## Definition

The exponentiation operator raises a number to the power of another number.

### Syntax

```python
result = operand1 ** operand2
```

---

### Example

```python
print(2 ** 5)
```

Output

```
32
```

---

### Example

```python
print(10 ** 2)
```

Output

```
100
```

---

### Real-world Example

Finding the area of a square.

```python
side = 8

area = side ** 2

print(area)
```

Output

```
64
```

---

# Floor Division Operator (//)

## Definition

The floor division operator divides two numbers and returns only the integer part of the quotient by removing the decimal portion.

### Syntax

```python
result = operand1 // operand2
```

---

### Example

```python
print(17 // 3)
```

Output

```
5
```

---

### Example

```python
print(25 // 4)
```

Output

```
6
```

---

### Difference Between / and //

| Operator | Description | Example | Output |
|----------|-------------|---------|--------|
| / | Normal Division | 10 / 3 | 3.333333 |
| // | Floor Division | 10 // 3 | 3 |

---

# Summary of Arithmetic Operators

| Operator | Name | Example |
|----------|------|---------|
| + | Addition | a + b |
| - | Subtraction | a - b |
| * | Multiplication | a * b |
| / | Division | a / b |
| % | Modulus | a % b |
| ** | Exponentiation | a ** b |
| // | Floor Division | a // b |

---

# Common Mistakes

- Using `/` instead of `//`.
- Trying to add strings and integers directly.
- Forgetting that `/` always returns a float.
- Using `%` incorrectly.

---

# Best Practices

- Use meaningful variable names.
- Convert data types before performing operations.
- Use parentheses in complex expressions.
- Use `%` for checking even/odd numbers.
- Use `**` instead of repeated multiplication.
# Assignment Operators

## What are Assignment Operators?

Assignment operators are used to assign values to variables. They can also perform an operation and assign the result back to the same variable.

These operators make code shorter, cleaner, and easier to read.

Example:

```python
x = 10
```

Here, the `=` operator assigns the value `10` to the variable `x`.

---

# Types of Assignment Operators

| Operator | Example | Equivalent Expression |
|----------|---------|-----------------------|
| = | x = 5 | x = 5 |
| += | x += 3 | x = x + 3 |
| -= | x -= 3 | x = x - 3 |
| *= | x *= 3 | x = x * 3 |
| /= | x /= 3 | x = x / 3 |
| %= | x %= 3 | x = x % 3 |
| //= | x //= 3 | x = x // 3 |
| **= | x **= 3 | x = x ** 3 |
| &= | x &= 3 | x = x & 3 |
| \|= | x \|= 3 | x = x \| 3 |
| ^= | x ^= 3 | x = x ^ 3 |
| >>= | x >>= 3 | x = x >> 3 |
| <<= | x <<= 3 | x = x << 3 |

---

# Assignment Operator (=)

## Definition

The assignment operator assigns a value to a variable.

### Syntax

```python
variable = value
```

### Example

```python
name = "Python"

print(name)
```

Output

```
Python
```

---

# Addition Assignment (+=)

## Definition

Adds a value and stores the result in the same variable.

### Example

```python
x = 10

x += 5

print(x)
```

Output

```
15
```

Equivalent to

```python
x = x + 5
```

---

# Subtraction Assignment (-=)

## Definition

Subtracts a value from the variable and stores the result.

### Example

```python
marks = 100

marks -= 15

print(marks)
```

Output

```
85
```

Equivalent to

```python
marks = marks - 15
```

---

# Multiplication Assignment (*=)

## Definition

Multiplies the variable by another value and stores the result.

### Example

```python
salary = 5000

salary *= 2

print(salary)
```

Output

```
10000
```

---

# Division Assignment (/=)

## Definition

Divides the variable by another value and stores the result.

### Example

```python
x = 20

x /= 4

print(x)
```

Output

```
5.0
```

---

# Modulus Assignment (%=)

## Definition

Stores the remainder after division.

### Example

```python
x = 25

x %= 4

print(x)
```

Output

```
1
```

---

# Floor Division Assignment (//=)

## Definition

Performs floor division and stores the integer quotient.

### Example

```python
x = 25

x //= 4

print(x)
```

Output

```
6
```

---

# Exponentiation Assignment (**=)

## Definition

Raises a number to a power and stores the result.

### Example

```python
x = 3

x **= 4

print(x)
```

Output

```
81
```

---

# Bitwise Assignment Operators

These operators combine bitwise operations with assignment.

Examples

```python
x = 5

x &= 3
```

```python
x = 5

x |= 3
```

```python
x = 5

x ^= 3
```

```python
x = 5

x >>= 1
```

```python
x = 5

x <<= 2
```

These are mainly used in low-level programming and binary manipulation.

---

# Why Use Assignment Operators?

Advantages:

- Shorter code
- Better readability
- Easier maintenance
- Faster coding

Instead of

```python
x = x + 1
```

use

```python
x += 1
```

---

# Common Mistakes

- Using `==` instead of `=`.
- Forgetting that `/=` returns a float.
- Using assignment operators before initializing variables.

Incorrect

```python
x += 5
```

Correct

```python
x = 10

x += 5
```

---

# Best Practices

- Initialize variables before using assignment operators.
- Use compound assignment operators to make code cleaner.
- Use meaningful variable names.

---

# Comparison Operators

## What are Comparison Operators?

Comparison operators compare two values and return either **True** or **False**.

They are mainly used in:

- if statements
- loops
- decision making
- logical expressions

---

# Types of Comparison Operators

| Operator | Name |
|----------|------|
| == | Equal To |
| != | Not Equal To |
| > | Greater Than |
| < | Less Than |
| >= | Greater Than or Equal To |
| <= | Less Than or Equal To |

---

# Equal To (==)

Checks whether two values are equal.

Example

```python
a = 20
b = 20

print(a == b)
```

Output

```
True
```

---

# Not Equal To (!=)

Checks whether two values are different.

Example

```python
a = 20
b = 15

print(a != b)
```

Output

```
True
```

---

# Greater Than (>)

Returns True if the left value is greater.

Example

```python
age = 21

print(age > 18)
```

Output

```
True
```

---

# Less Than (<)

Returns True if the left value is smaller.

Example

```python
temperature = 18

print(temperature < 25)
```

Output

```
True
```

---

# Greater Than or Equal To (>=)

Returns True if the value is greater than or equal.

Example

```python
marks = 75

print(marks >= 35)
```

Output

```
True
```

---

# Less Than or Equal To (<=)

Returns True if the value is less than or equal.

Example

```python
stock = 5

print(stock <= 10)
```

Output

```
True
```

---

# Real-world Example

```python
age = 19

if age >= 18:
    print("Eligible for Driving License")
else:
    print("Not Eligible")
```

Output

```
Eligible for Driving License
```

---

# Common Mistakes

- Confusing `=` with `==`.
- Comparing incompatible data types.
- Forgetting that comparison operators always return a Boolean value.

---

# Best Practices

- Use comparison operators inside conditional statements.
- Use parentheses for complex expressions.
- Compare values of compatible data types whenever possible.
# Logical Operators

## What are Logical Operators?

Logical operators are used to combine two or more conditional expressions. They return either **True** or **False** depending on the conditions.

Logical operators are commonly used in:

- Decision making
- if statements
- while loops
- User authentication
- Input validation

Python provides three logical operators.

| Operator | Description |
|----------|-------------|
| and | Returns True if both conditions are True |
| or | Returns True if at least one condition is True |
| not | Reverses the Boolean value |

---

# AND Operator (and)

## Definition

The **and** operator returns **True** only if **both conditions are True**.

### Syntax

```python
condition1 and condition2
```

### Example

```python
age = 22
has_license = True

print(age >= 18 and has_license)
```

Output

```
True
```

---

### Example

```python
print(10 > 5 and 20 > 30)
```

Output

```
False
```

---

### Real-world Example

```python
username = "admin"
password = "python123"

if username == "admin" and password == "python123":
    print("Login Successful")
else:
    print("Invalid Credentials")
```

Output

```
Login Successful
```

---

# OR Operator (or)

## Definition

The **or** operator returns **True** if at least one condition is True.

### Syntax

```python
condition1 or condition2
```

---

### Example

```python
print(10 > 20 or 15 > 10)
```

Output

```
True
```

---

### Example

```python
age = 16

print(age >= 18 or age >= 16)
```

Output

```
True
```

---

### Real-world Example

```python
is_admin = False
is_teacher = True

if is_admin or is_teacher:
    print("Access Granted")
```

Output

```
Access Granted
```

---

# NOT Operator (not)

## Definition

The **not** operator reverses the Boolean value.

- True becomes False
- False becomes True

### Syntax

```python
not condition
```

---

### Example

```python
print(not True)
```

Output

```
False
```

---

### Example

```python
age = 15

print(not(age >= 18))
```

Output

```
True
```

---

### Real-world Example

```python
logged_in = False

if not logged_in:
    print("Please Login")
```

Output

```
Please Login
```

---

# Truth Table

| Condition 1 | Condition 2 | and | or |
|--------------|-------------|-----|----|
| True | True | True | True |
| True | False | False | True |
| False | True | False | True |
| False | False | False | False |

---

# Common Mistakes

- Confusing **and** with **or**.
- Forgetting to use parentheses in complex conditions.
- Using **not** incorrectly.

Incorrect

```python
not age > 18 and age < 30
```

Better

```python
not (age > 18 and age < 30)
```

---

# Best Practices

- Use parentheses for better readability.
- Keep logical expressions simple.
- Break long conditions into multiple variables.

---

# Identity Operators

## What are Identity Operators?

Identity operators compare whether two variables refer to the **same object in memory**, not just whether their values are equal.

Python provides two identity operators.

| Operator | Description |
|----------|-------------|
| is | Returns True if both variables refer to the same object |
| is not | Returns True if both variables refer to different objects |

---

# is Operator

## Definition

The **is** operator checks whether two variables refer to the same object in memory.

### Example

```python
a = [1,2,3]
b = a

print(a is b)
```

Output

```
True
```

---

### Example

```python
a = [1,2,3]
b = [1,2,3]

print(a is b)
```

Output

```
False
```

Although both lists have the same values, they are stored in different memory locations.

---

# Difference Between == and is

Example

```python
a = [1,2]
b = [1,2]

print(a == b)
print(a is b)
```

Output

```
True
False
```

Explanation

- `==` compares values.
- `is` compares object identity (memory location).

---

# is not Operator

## Definition

Returns True if two variables do not refer to the same object.

Example

```python
a = [1]
b = [1]

print(a is not b)
```

Output

```
True
```

---

### Real-world Example

Checking whether a variable is None.

```python
name = None

if name is None:
    print("No Name Found")
```

Output

```
No Name Found
```

Using `is None` is the recommended Python style.

---

# Common Mistakes

Many beginners think

```python
a == b
```

and

```python
a is b
```

mean the same thing.

They do not.

- `==` compares values.
- `is` compares memory locations.

---

# Best Practices

- Use `==` to compare values.
- Use `is` only when checking object identity.
- Use `is None` instead of `== None`.

---

# Membership Operators

## What are Membership Operators?

Membership operators are used to check whether a value exists inside a sequence or collection.

Python provides two membership operators.

| Operator | Description |
|----------|-------------|
| in | Returns True if the value exists |
| not in | Returns True if the value does not exist |

Membership operators work with:

- Strings
- Lists
- Tuples
- Sets
- Dictionaries

---

# in Operator

## Definition

Returns True if the specified value is present.

### Example

```python
fruits = ["Apple","Banana","Mango"]

print("Banana" in fruits)
```

Output

```
True
```

---

### Example with String

```python
text = "Python Programming"

print("Python" in text)
```

Output

```
True
```

---

### Example with Dictionary

```python
student = {
    "name":"John",
    "age":20
}

print("name" in student)
```

Output

```
True
```

Note:

For dictionaries, membership checks **keys**, not values.

---

# not in Operator

## Definition

Returns True if the specified value is not present.

### Example

```python
numbers = [10,20,30]

print(40 not in numbers)
```

Output

```
True
```

---

### Example

```python
text = "Python"

print("Java" not in text)
```

Output

```
True
```

---

# Real-world Example

```python
username = "admin"

allowed_users = ["admin","teacher","student"]

if username in allowed_users:
    print("Access Granted")
else:
    print("Access Denied")
```

Output

```
Access Granted
```

---

# Common Mistakes

- Checking dictionary values instead of keys.
- Using membership operators on unsupported data types.

---

# Best Practices

- Use `in` for checking existence instead of writing long comparison statements.
- Use membership operators to improve readability.
- Remember that dictionaries check keys by default.
# Bitwise Operators

## What are Bitwise Operators?

Bitwise operators perform operations on the binary (bit-level) representation of integers. They are commonly used in low-level programming, networking, cryptography, image processing, embedded systems, and performance optimization.

Before learning bitwise operators, it is useful to understand binary numbers.

Example:

```python
a = 5
```

Binary representation of 5 is:

```
00000101
```

---

# Types of Bitwise Operators

| Operator | Name | Description |
|----------|------|-------------|
| & | AND | Sets a bit to 1 if both bits are 1 |
| \| | OR | Sets a bit to 1 if at least one bit is 1 |
| ^ | XOR | Sets a bit to 1 if bits are different |
| ~ | NOT | Inverts all bits |
| << | Left Shift | Shifts bits to the left |
| >> | Right Shift | Shifts bits to the right |

---

# Bitwise AND (&)

Returns 1 only if both bits are 1.

Example

```python
a = 5
b = 3

print(a & b)
```

Output

```
1
```

Binary Explanation

```
5 = 101
3 = 011

-----------
    001
```

---

# Bitwise OR (|)

Returns 1 if at least one bit is 1.

Example

```python
a = 5
b = 3

print(a | b)
```

Output

```
7
```

Binary

```
101
011
---
111
```

---

# Bitwise XOR (^)

Returns 1 only when bits are different.

Example

```python
a = 5
b = 3

print(a ^ b)
```

Output

```
6
```

Binary

```
101
011
---
110
```

---

# Bitwise NOT (~)

Inverts all bits.

Example

```python
print(~5)
```

Output

```
-6
```

---

# Left Shift (<<)

Moves bits to the left.

Example

```python
print(5 << 1)
```

Output

```
10
```

Another Example

```python
print(5 << 2)
```

Output

```
20
```

---

# Right Shift (>>)

Moves bits to the right.

Example

```python
print(20 >> 2)
```

Output

```
5
```

---

# Real-world Uses of Bitwise Operators

Bitwise operators are commonly used in:

- Cryptography
- Image Processing
- Network Programming
- Embedded Systems
- Permission Management
- Performance Optimization

---

# Operator Precedence

## What is Operator Precedence?

Operator precedence determines the order in which operations are performed in an expression.

Example

```python
result = 10 + 5 * 2

print(result)
```

Output

```
20
```

Explanation

Multiplication has higher precedence than addition.

Equivalent expression

```python
10 + (5 * 2)
```

---

Example

```python
print((10 + 5) * 2)
```

Output

```
30
```

---

## Operator Precedence Table

| Priority | Operators |
|-----------|-----------|
| Highest | () |
| | ** |
| | +x, -x, ~x |
| | *, /, //, % |
| | +, - |
| | <<, >> |
| | & |
| | ^ |
| | \| |
| | ==, !=, >, <, >=, <= |
| | not |
| | and |
| Lowest | or |

---

# Overall Common Mistakes

Many beginners make the following mistakes:

- Using `=` instead of `==`.
- Confusing `is` with `==`.
- Forgetting that `/` always returns a float.
- Expecting sets to maintain order while using membership operators.
- Using assignment operators before initializing variables.
- Forgetting operator precedence.
- Mixing logical operators without parentheses.
- Incorrectly using bitwise operators instead of logical operators.

---

# Overall Best Practices

- Use meaningful variable names.
- Use parentheses in complex expressions.
- Prefer `+=` instead of `x = x + value`.
- Use `is None` instead of `== None`.
- Use `==` for value comparison.
- Use `is` only for object identity.
- Use membership operators for checking existence.
- Write simple and readable expressions.
- Avoid unnecessary nested conditions.

---

# Frequently Asked Questions (FAQs)

### 1. What are operators in Python?

Operators are symbols used to perform operations on values and variables.

### 2. How many types of operators are there?

Python provides seven categories of operators.

### 3. What is the difference between `=` and `==`?

`=` assigns a value, whereas `==` compares two values.

### 4. What is the difference between `/` and `//`?

`/` performs normal division and returns a float.

`//` performs floor division and returns the integer quotient.

### 5. What is `%` used for?

It returns the remainder after division.

### 6. What is `**`?

It is the exponentiation operator.

### 7. Difference between `is` and `==`?

`==` compares values.

`is` compares memory locations.

### 8. What does `in` do?

Checks whether a value exists in a sequence.

### 9. What does `not in` do?

Checks whether a value does not exist.

### 10. What are bitwise operators?

They operate directly on binary numbers.

### 11. Which operator has the highest precedence?

Parentheses `()`.

### 12. Why should parentheses be used?

They improve readability and avoid precedence-related errors.

---

# Interview Questions

1. What are operators in Python?
2. Explain different types of operators.
3. Difference between `=` and `==`.
4. Difference between `/` and `//`.
5. Difference between `is` and `==`.
6. Explain logical operators.
7. Explain membership operators.
8. What are identity operators?
9. What are bitwise operators?
10. Explain operator precedence.
11. What is floor division?
12. Explain modulus with an example.
13. What is exponentiation?
14. Difference between `and` and `or`.
15. What is `not` operator?
16. What is `+=`?
17. Explain comparison operators.
18. Give real-world applications of bitwise operators.
19. Why is operator precedence important?
20. What are the most common mistakes while using operators?

---

# Summary

Operators are one of the most fundamental concepts in Python programming. They enable programmers to perform arithmetic calculations, compare values, assign variables, evaluate logical conditions, check membership, compare object identities, and manipulate binary data. Understanding operators and their precedence is essential for writing efficient, readable, and error-free Python programs. Choosing the correct operator for a given task improves code quality, maintainability, and overall program performance.