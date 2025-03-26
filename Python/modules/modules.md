# 📦 Python Modules – Complete Guide

In Python, a **module** is simply a Python file (`.py`) containing reusable functions, variables, and classes. Modules allow you to organize your code logically, making it easy to manage, reuse, and maintain.

---

## 🚀 Why Use Modules?

- Reuse code across different projects
- Keep your code organized and easy to maintain
- Improve readability and reduce complexity

---

## 🔹 What is a Module?

A module is any Python script saved with a `.py` extension. You can import this file in another Python script to access its functions and variables.

### ✅ Simple Module Example (`mymodule.py`)

```python
# mymodule.py

def greet(name):
    print(f"Hello, {name}!")

person = {"name": "Alice", "age": 30}
```

---

## 🔹 Importing Modules

To use a module, import it with the `import` keyword:

```python
import mymodule

mymodule.greet("Bob")  # Output: Hello, Bob!
print(mymodule.person)  # Output: {'name': 'Alice', 'age': 30}
```

### ✅ Using `from` Import

```python
from mymodule import greet, person

greet("Charlie")  # Output: Hello, Charlie!
print(person["name"])  # Output: Alice
```

---

## 📚 Built-in Modules (Quick Links)

- [🔗 Math Module](#math-module)
- [🔗 Random Module](#random-module)
- [🔗 Datetime Module](#datetime-module)
- [🔗 OS Module](#os-module)
- [🔗 Sys Module](#sys-module)
- [🔗 Platform Module](#platform-module)

### ✅ <a id="math-module"></a>The `math` Module
Perform mathematical operations easily.

```python
import math

print(math.sqrt(16))  # Output: 4.0
print(math.pi)        # Output: 3.141592653589793
```

### ✅ <a id="random-module"></a>The `random` Module
Generate random numbers or choose random items.

```python
import random

# Random integer
print(random.randint(1, 10))  # Random integer between 1 and 10

# Random choice from list
fruits = ['apple', 'banana', 'cherry']
print(random.choice(fruits))
```

### ✅ <a id="datetime-module"></a>The `datetime` Module
Handle dates and times in Python.

```python
import datetime

# Current date and time
now = datetime.datetime.now()
print("Now:", now)

# Specific date
date = datetime.datetime(2024, 12, 25)
print("Christmas:", date.strftime("%Y-%m-%d"))
```

### ✅ <a id="os-module"></a>The `os` Module
Interact with your operating system.

```python
import os

# Current working directory
print("Current Directory:", os.getcwd())

# List files
print("Files:", os.listdir())
```

### ✅ <a id="sys-module"></a>The `sys` Module
Interact with the Python interpreter.

```python
import sys

# Python version
print("Python Version:", sys.version)

# Command line arguments
print("Arguments:", sys.argv)
```

### ✅ <a id="platform-module"></a>The `platform` Module
Get system information easily.

```python
import platform

print("System:", platform.system())
print("Version:", platform.version())
print("Processor:", platform.processor())
print("Python Version:", platform.python_version())
```

---

## 🛠️ User-Defined Modules

You can easily create your own modules for reusable code.

### ✅ Create Your Own Module (`calculator.py`)

```python
# calculator.py

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b
```

### ✅ Use Your Module

```python
import calculator

print("Addition:", calculator.add(10, 5))       # Output: 15
print("Subtraction:", calculator.subtract(10, 5)) # Output: 5
```

---

## 📦 Creating and Using Packages

Packages organize multiple modules into directories:

```bash
mypackage/
├── __init__.py
├── module1.py
└── module2.py
```

### ✅ Example Usage

```python
from mypackage import module1

module1.some_function()
```

---

## 🔹 Aliasing Modules

Create aliases for easier access:

```python
import math as m

print(m.pi)
```

---

## 🔍 The `dir()` Function

Explore available functions and attributes in a module:

```python
import math
print(dir(math))
```

---

## 📌 Quick Reference Table

| Operation                    | Example                                   |
|------------------------------|-------------------------------------------|
| Import module                | `import module`                           |
| Import specific functions    | `from module import function`             |
| Alias a module               | `import module as alias`                  |
| Common built-in modules      | `math`, `random`, `datetime`, `os`, `sys`, `platform` |
| Use `dir()`                  | `dir(module)`                             |

---
