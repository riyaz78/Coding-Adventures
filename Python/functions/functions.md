# 📘 Python Functions – Complete Guide

Functions in Python are blocks of reusable code that perform a specific task. They help make your code modular, readable, and maintainable.

---

## 🔹 What is a Function?

A function is a reusable block of code that only runs when it is called. You can pass data into a function and receive output.

### ✅ Basic Function Syntax

```python
def function_name(parameters):
    # code block
    return value
```

### ✅ Example
```python
def greet():
    print("Hello!")

greet()  # Output: Hello!
```

---

## 🔹 Why Use Functions?
- Avoid code repetition
- Increase readability and reusability
- Organize code into logical blocks
- Break down complex problems into simpler parts

---

## 🔹 Function with Parameters

Parameters are placeholders for values you pass into the function.

```python
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")  # Output: Hello, Alice!
```

### ✅ Multiple Parameters
```python
def add(a, b):
    print(a + b)

add(5, 3)  # Output: 8
```

---

## 🔹 Function with Return Value

Use `return` to send data back from a function:

```python
def multiply(a, b):
    return a * b

result = multiply(4, 5)
print(result)  # Output: 20
```

---

## 🔹 Default Parameter Values

If no argument is passed, the default value is used:

```python
def greet(name="Guest"):
    print(f"Hello, {name}!")

greet()          # Hello, Guest!
greet("John")    # Hello, John!
```

---

## 🔹 Keyword Arguments

You can specify arguments using their parameter names:

```python
def describe_pet(animal, name):
    print(f"I have a {animal} named {name}.")

describe_pet(name="Whiskers", animal="cat")
```

---

## 🔹 Variable-Length Arguments

### `*args` – Non-keyworded (Tuple)
```python
def print_numbers(*args):
    for num in args:
        print(num)

print_numbers(1, 2, 3)
```

### `**kwargs` – Keyworded (Dictionary)
```python
def print_profile(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_profile(name="Alice", age=30)
```

---

## 🔹 Scope of Variables

### Local Scope
Defined inside a function and only accessible within that function.

### Global Scope
Defined outside all functions and accessible globally.

```python
x = 10  # Global

def my_func():
    y = 5  # Local
    print("x:", x)

my_func()
# print(y)  # Error: y is not defined outside
```

### Modifying Global Variables
Use `global` keyword:
```python
def modify():
    global x
    x = 20
```

---

## 🔹 Lambda Functions

A lambda function is an anonymous, single-expression function:

```python
square = lambda x: x * x
print(square(5))  # 25
```

### ✅ Use Case
Use lambda for short, one-liner functions, especially in `map()`, `filter()`, and `sorted()`:

```python
nums = [1, 2, 3, 4]
squared = list(map(lambda x: x*x, nums))
print(squared)
```

---

## 🔹 Nested Functions

A function defined inside another:

```python
def outer():
    def inner():
        print("Inner function")
    print("Outer function")
    inner()

outer()
```

---

## 🔹 Higher-Order Functions

A function that takes another function as an argument or returns one.

```python
def shout(text):
    return text.upper()

def whisper(text):
    return text.lower()

def speak(style_func):
    return style_func("Hello")

print(speak(shout))   # HELLO
print(speak(whisper)) # hello
```

---

## 🔹 Recursion

A function that calls itself.

```python
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))  # 120
```

> Be cautious with recursion: ensure a base case exists to avoid infinite calls.

---

## 🔹 Docstrings

Use triple quotes to document your function:

```python
def add(a, b):
    """Returns the sum of a and b."""
    return a + b

print(add.__doc__)
```

---

## 📌 Summary Table

| Feature                      | Example                                      |
|------------------------------|----------------------------------------------|
| Basic Function               | `def greet():`                               |
| With Parameters              | `def greet(name):`                           |
| Return Value                 | `return a + b`                               |
| Default Parameters           | `def greet(name="Guest"):`                  |
| *args                        | `def func(*args):`                           |
| **kwargs                     | `def func(**kwargs):`                        |
| Lambda                       | `lambda x: x + 1`                            |
| Nested                       | Function inside another                     |
| Higher-Order Function        | Takes/returns another function              |
| Recursive Function           | Calls itself                                 |
| Docstring                    | `"""Function description"""`                |

---

## 🧪 Practice Examples

```python
# 1. Basic function
def say_hello():
    print("Hello, world!")

# 2. Function with arguments and return
def power(base, exponent):
    return base ** exponent

# 3. Using *args
def total_sum(*numbers):
    return sum(numbers)

# 4. Using **kwargs
def person_details(**info):
    for key, value in info.items():
        print(f"{key}: {value}")

# 5. Lambda + map
nums = [1, 2, 3]
squares = list(map(lambda x: x*x, nums))
print(squares)
```

