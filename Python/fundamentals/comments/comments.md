# 📘 Python Comments – Complete Guide

In Python, **comments** are used to explain code, make it more readable, and help with future maintenance. They are ignored by the Python interpreter and do not affect program execution.

---

## 🔹 Why Use Comments?
- To explain complex logic.
- To document what specific sections of code do.
- To temporarily disable parts of code during debugging.
- For better collaboration and readability.

---

## 🔸 Single-line Comments

Use the `#` symbol. Everything after `#` on the same line is ignored by Python.

```python
# This is a single-line comment
print("Hello")  # This prints a greeting
```

---

## 🔸 Multi-line Comments (Block Comments)

Python doesn’t have a specific multi-line comment syntax like some other languages, but there are **two common ways** to achieve this:

### ✅ Option 1: Multiple `#` symbols
```python
# This is a multi-line comment
# spread over several lines
# using the hash symbol
```

### ✅ Option 2: Triple quotes (technically strings, but often used this way)
```python
'''
This is a multi-line comment
written using triple single quotes
'''

"""
This is another multi-line comment
using triple double quotes
"""
```
> ⚠️ Note: Triple quotes create **string literals**, not true comments. They are ignored if not assigned to a variable, but should be used primarily for docstrings.

---

## 🔸 Docstrings vs Comments

- Docstrings are special strings that document modules, functions, classes, or methods.
- They are defined using triple quotes and are placed as the first statement in a function/module/class.
- You can access them with the `__doc__` attribute.

```python
def greet():
    """This function prints a greeting message."""
    print("Hello")

print(greet.__doc__)
```

---

## 📌 Summary Table

| Type              | Symbol/Method        | Notes                                      |
|-------------------|----------------------|--------------------------------------------|
| Single-line       | `#`                  | Most commonly used comment style            |
| Multi-line        | `#` per line         | Multiple `#`s across lines                 |
| Multi-line (alt)  | `'''` or `"""`       | Not true comments, used for docstrings      |
| Docstrings        | `'''` or `"""`       | Used inside functions, modules, classes     |

---
