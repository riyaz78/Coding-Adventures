
# 📘 Python Literals – Complete Guide

In Python, **literals** represent fixed values that are assigned to variables or used directly in code. They are the most basic building blocks of Python syntax.

---

## 🔹 Types of Literals

Python supports the following types of literals:

- **String Literals**
- **Numeric Literals**
- **Boolean Literals**
- **Special Literal: `None`**
- **Literal Collections** (List, Tuple, Set, Dictionary)

---

## 🔸 1. String Literals

String literals represent sequences of characters. They can be enclosed in:
- Single quotes (`'Hello'`)
- Double quotes (`"World"`)
- Triple quotes for multi-line strings (`'''Line1\nLine2'''`)

```python
s1 = 'Hello'
s2 = "World"
s3 = '''Multi-line
String'''
```

---

## 🔸 2. Numeric Literals

Python supports different kinds of numeric literals:

- **Integer:** `10`, `-200`
- **Float:** `3.14`, `-0.001`
- **Complex:** `3 + 4j`

```python
x = 10        # Integer
pi = 3.14     # Float
z = 2 + 3j    # Complex
```

---

## 🔸 3. Boolean Literals

Boolean literals represent truth values:

```python
is_active = True
is_admin = False
```

These are internally treated as integers (`True == 1`, `False == 0`).

---

## 🔸 4. Special Literal: `None`

`None` is a special literal that represents the absence of a value.

```python
result = None
```

It’s commonly used as a default return type or to reset variables.

---

## 🔸 5. Literal Collections

Python supports collection literals like:

### List Literal:
```python
fruits = ['apple', 'banana', 'cherry']
```

### Tuple Literal:
```python
point = (10, 20)
```

### Set Literal:
```python
unique_ids = {101, 102, 103}
```

### Dictionary Literal:
```python
person = {'name': 'Alice', 'age': 25}
```

---

## 📌 Summary Table

| Type             | Example                          |
|------------------|----------------------------------|
| String Literal   | `'Hello'`, `"World"`             |
| Integer Literal  | `10`, `-5`                       |
| Float Literal    | `3.14`, `-0.001`                 |
| Complex Literal  | `2 + 3j`                         |
| Boolean Literal  | `True`, `False`                  |
| Special Literal  | `None`                           |
| List Literal     | `[1, 2, 3]`                      |
| Tuple Literal    | `(1, 2, 3)`                      |
| Set Literal      | `{1, 2, 3}`                      |
| Dictionary Literal | `{'key': 'value'}`            |

