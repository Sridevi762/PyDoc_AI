# Control Flow

## What is Control Flow?

Control flow refers to the order in which statements and instructions are executed in a Python program. By default, Python executes code sequentially from top to bottom. However, there are situations where a program needs to make decisions, repeat certain tasks, or skip parts of the code. Control flow statements make this possible.

Control flow enables programs to respond dynamically to different conditions and user inputs, making applications interactive and intelligent.

---

## Why is Control Flow Important?

Control flow is one of the fundamental concepts of programming because it allows developers to:

- Make decisions based on conditions.
- Execute different blocks of code depending on user input.
- Repeat tasks without writing duplicate code.
- Improve program efficiency and readability.
- Build real-world applications such as login systems, banking software, games, and automation scripts.

Without control flow, programs would execute every statement in sequence without making decisions or repeating tasks.

---

## Types of Control Flow

Python provides three main categories of control flow:

1. Decision Making Statements
2. Looping Statements
3. Loop Control Statements

---

# Decision Making Statements

Decision-making statements allow Python to execute different blocks of code depending on whether a condition is True or False.

Python provides the following decision-making statements:

- if
- if...else
- if...elif...else
- Nested if
- match (Python 3.10+)

---

# if Statement

## Definition

The `if` statement is the simplest decision-making statement in Python. It executes a block of code only when a specified condition evaluates to `True`.

If the condition evaluates to `False`, Python skips the indented block and continues executing the remaining program.

---

## Syntax

```python
if condition:
    statements
```

---

## Flow

1. Evaluate the condition.
2. If the condition is True, execute the indented block.
3. If the condition is False, skip the block.
4. Continue with the remaining statements.

---

## Example 1

```python
age = 20

if age >= 18:
    print("Eligible to vote")
```

### Output

```
Eligible to vote
```

### Explanation

Since the value of `age` is greater than or equal to 18, the condition evaluates to True, so Python executes the print statement.

---

## Example 2

```python
number = 10

if number > 0:
    print("Positive Number")
```

### Output

```
Positive Number
```

---

## Example 3

```python
temperature = 35

if temperature > 30:
    print("It's a hot day.")
```

### Output

```
It's a hot day.
```

---

## Real-world Example

Checking whether a customer is eligible for a discount.

```python
purchase_amount = 2500

if purchase_amount >= 2000:
    print("Discount Applied")
```

Output

```
Discount Applied
```

---

## Common Mistakes

### Using = instead of ==

Incorrect

```python
if age = 18:
    print("Adult")
```

This produces a SyntaxError.

Correct

```python
if age == 18:
    print("Adult")
```

---

### Forgetting Indentation

Incorrect

```python
if age >= 18:
print("Adult")
```

Output

```
IndentationError
```

Correct

```python
if age >= 18:
    print("Adult")
```

---

## Best Practices

- Write clear and readable conditions.
- Keep the code inside the if block properly indented.
- Avoid writing unnecessary nested if statements.
- Use meaningful variable names.

---

# if...else Statement

## Definition

The `if...else` statement is used when there are two possible outcomes. If the condition is True, the `if` block executes; otherwise, the `else` block executes.

Only one block executes during program execution.

---

## Syntax

```python
if condition:
    statements
else:
    statements
```

---

## Example 1

```python
age = 16

if age >= 18:
    print("Eligible to Vote")
else:
    print("Not Eligible")
```

### Output

```
Not Eligible
```

---

## Example 2

```python
number = 7

if number % 2 == 0:
    print("Even")
else:
    print("Odd")
```

### Output

```
Odd
```

---

## Example 3

```python
password = "python123"

if password == "python123":
    print("Login Successful")
else:
    print("Incorrect Password")
```

### Output

```
Login Successful
```

---

## Explanation

Python first checks the condition.

- If True → execute the if block.
- If False → execute the else block.

Only one of the two blocks is executed.

---

## Real-world Applications

- ATM PIN Verification
- Login Authentication
- Age Verification
- Exam Result Systems
- Shopping Discount Eligibility

---

## Common Mistakes

- Forgetting the colon (:)
- Incorrect indentation
- Using assignment operator (=) instead of comparison operator (==)

---

## Best Practices

- Keep conditions simple.
- Avoid writing complex expressions inside the condition.
- Use meaningful messages.

---

# if...elif...else Statement

## Definition

The `if...elif...else` statement is used when multiple conditions need to be evaluated.

Python checks each condition from top to bottom.

The first condition that evaluates to True is executed, and the remaining conditions are skipped.

If none of the conditions are True, the else block executes.

---

## Syntax

```python
if condition1:
    statements

elif condition2:
    statements

elif condition3:
    statements

else:
    statements
```

---

## Example

```python
marks = 82

if marks >= 90:
    print("Grade A")

elif marks >= 75:
    print("Grade B")

elif marks >= 60:
    print("Grade C")

else:
    print("Fail")
```

### Output

```
Grade B
```

---

## Explanation

Python checks the conditions in order.

- Is marks >= 90? ❌ No
- Is marks >= 75? ✅ Yes

Python executes that block and ignores the remaining conditions.

---

## Real-world Example

Employee Bonus System

```python
salary = 80000

if salary >= 100000:
    print("20% Bonus")

elif salary >= 70000:
    print("10% Bonus")

else:
    print("5% Bonus")
```

Output

```
10% Bonus
```

---

## Common Mistakes

- Writing conditions in the wrong order.
- Using multiple separate if statements instead of elif.
- Forgetting indentation.

---

## Best Practices

- Place the most specific conditions first.
- Keep the number of elif statements reasonable.
- Use match statement for many fixed values (Python 3.10+).

---

# Nested if Statement

## Definition

A Nested if statement is an if statement placed inside another if statement.

Nested if statements are used when multiple conditions depend on one another.

## Syntax

```python
if condition1:
    if condition2:
        statements
```

## Example

```python
age = 22
citizen = True

if age >= 18:
    if citizen:
        print("Eligible to Vote")
```

### Output

```
Eligible to Vote

## Explanation

The second if statement is checked only if the first condition is True.

## Real-world Example

Online Banking

- User enters correct password.
- Then OTP verification is checked.

Only after both conditions are satisfied can the user access the account.
