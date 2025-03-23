# 🐍 Python Errors and Exceptions – Complete Guide

Errors and exceptions are integral to programming. They help identify and handle unexpected situations during code execution, ensuring your programs run reliably and predictably.

---

## 🔹 Types of Errors in Python

### ✅ Syntax Errors
Occurs when Python encounters incorrect syntax (typos, missing colons, parentheses, etc.).

```python
# Example of Syntax Error (missing colon)
if True
    print("Hello")
# Output: SyntaxError: expected ':'
```

### ✅ Runtime Errors (Exceptions)
Occurs during program execution, causing the program to stop unless explicitly handled.

```python
# Example of Runtime Error
x = 10 / 0  # ZeroDivisionError
```

---

## 🔹 Common Built-in Exceptions

| Exception Type         | Description                                        | Example                            |
|------------------------|----------------------------------------------------|------------------------------------|
| `ZeroDivisionError`    | Division by zero                                   | `10 / 0`                           |
| `TypeError`            | Operation between incompatible types               | `'2' + 2`                          |
| `ValueError`           | Invalid value conversion                           | `int("abc")`                      |
| `IndexError`           | List index out-of-range                            | `[1,2,3][3]`                       |
| `KeyError`             | Non-existent dictionary key                        | `d = {'a':1}; d['b']`              |
| `NameError`            | Undefined variable                                 | `print(x)` (if x undefined)        |
| `FileNotFoundError`    | File does not exist                                | `open("no_file.txt")`             |
| `AttributeError`       | Object lacks specified attribute                   | `[].appendd(1)`                    |
| `AssertionError`       | Failed assert statement                            | `assert x > 0` (if x<=0>)                    |

---

## 🔹 Exception Hierarchy

Python exceptions follow a hierarchical structure. Here's a simplified hierarchy:

```
BaseException
 ├── Exception
 │    ├── ArithmeticError
 │    │     ├── ZeroDivisionError
 │    │     └── OverflowError
 │    ├── LookupError
 │    │     ├── IndexError
 │    │     └── KeyError
 │    ├── ValueError
 │    ├── TypeError
 │    ├── NameError
 │    ├── FileNotFoundError
 │    ├── AttributeError
 │    └── AssertionError
 └── SystemExit
```

- `BaseException` is the root for all exceptions.
- Most user-defined and built-in exceptions inherit from `Exception`.

---

## 🔹 Handling Exceptions Using `try-except`

```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")
```

Handle multiple exceptions separately:

```python
try:
    num = int(input("Enter a number: "))
    result = 10 / num
except ValueError:
    print("Please enter a valid integer.")
except ZeroDivisionError:
    print("Cannot divide by zero.")
```

---

## 🔹 `else` and `finally` Blocks

### ✅ `else`
Executes if no exception occurs.

```python
try:
    x = 10 / 2
except ZeroDivisionError:
    print("Division error")
else:
    print("Division successful:", x)
```

### ✅ `finally`
Always executes, regardless of exceptions.

```python
try:
    file = open("sample.txt", "r")
    content = file.read()
except FileNotFoundError:
    print("File not found.")
finally:
    print("Attempted to read file.")
```

---


## 🔹 Assertion Errors

An `AssertionError` occurs when an `assert` statement fails.

```python
x = -5
assert x >= 0, "x should be positive"
# Output: AssertionError: x should be positive
```

- `assert` statements are typically used for debugging purposes, helping to validate assumptions in the code.

---

## 🔹 Catching Multiple Exceptions in One Block

```python
try:
    value = int(input("Enter a divisor: "))
    print(10 / value)
except (ValueError, ZeroDivisionError) as error:
    print("Error occurred:", error)
```

---

## 🔹 Raising Exceptions Manually

You can raise an exception explicitly using `raise`:

```python
age = -1
if age < 0:
    raise ValueError("Age cannot be negative.")
```

---

## 🔹 Creating Custom Exceptions

Define your custom exception by extending the `Exception` class:

```python
class NegativeAgeError(Exception):
    def __init__(self, age, message="Age cannot be negative"):
        self.age = age
        self.message = message
        super().__init__(self.message)

age = -5
if age < 0:
    raise NegativeAgeError(age)
```

---

## 📌 Summary Table

| Concept                | Syntax Example                                     |
|------------------------|----------------------------------------------------|
| try-except             | `try: ... except Exception:`                       |
| Multiple except blocks | `except TypeError:`                                |
| else block             | `else: print("Executed if no exception.")`        |
| finally block          | `finally: print("Always executes.")`              |
| Raise exception        | `raise ValueError("Error message")`               |
| Custom exception       | `class CustomError(Exception): pass`               |

---

## 🧪 Advanced Practice Examples

```python
# Handling file operations
try:
    with open("data.txt", "r") as file:
        lines = file.readlines()
except FileNotFoundError:
    print("Data file not found!")
else:
    print(lines)

# Custom exception usage
class InvalidScoreError(Exception):
    pass

score = 120
if not 0 <= score <= 100:
    raise InvalidScoreError("Score must be between 0 and 100.")
```
