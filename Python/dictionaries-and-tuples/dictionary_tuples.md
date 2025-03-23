# 📘 Python Dictionaries and Tuples – Complete Guide

This guide covers two important Python data structures: **Dictionaries** and **Tuples**.

---

# 🧾 Dictionaries in Python

Dictionaries are **ordered**, **mutable**, and **indexed** collections used to store **key-value pairs**.

---

## 🔹 Creating a Dictionary

```python
# Using curly braces
person = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}

# Using dict() constructor
data = dict(id=101, status="active")
```

---

## 🔹 Accessing Dictionary Values

```python
print(person["name"])       # Alice
print(person.get("age"))    # 25
```

> `get()` is safer than direct indexing as it avoids KeyError.

---

## 🔹 Modifying and Adding Items

```python
# Modify existing
person["age"] = 26

# Add new key-value
person["email"] = "alice@example.com"
```

---

## 🔹 Removing Items

```python
person.pop("city")      # Remove by key
del person["email"]     # Delete key-value pair
person.clear()          # Remove all items
```

---

## 🔹 Useful Dictionary Methods

```python
person = {"name": "Bob", "age": 30}

print(person.keys())     # dict_keys(['name', 'age'])
print(person.values())   # dict_values(['Bob', 30])
print(person.items())    # dict_items([('name', 'Bob'), ('age', 30)])

# Update existing dictionary
person.update({"city": "LA"})
```

---

## 🔹 Looping Through Dictionaries

```python
for key in person:
    print(key, person[key])

for key, value in person.items():
    print(f"{key}: {value}")
```

---

## 🔹 Nested Dictionaries

```python
users = {
    "user1": {"name": "Alice", "age": 25},
    "user2": {"name": "Bob", "age": 30}
}

print(users["user1"]["name"])  # Alice
```

---

## 🔹 Dictionary Comprehension

```python
squares = {x: x*x for x in range(1, 6)}
print(squares)  # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
```

With conditions:
```python
even_squares = {x: x*x for x in range(10) if x % 2 == 0}
```

---

## 📌 Dictionary Summary Table

| Operation               | Syntax                                  |
|-------------------------|-----------------------------------------|
| Create dictionary       | `d = {"a": 1, "b": 2}`                  |
| Access value            | `d["a"]`, `d.get("a")`                  |
| Add / Update key        | `d["c"] = 3`                             |
| Remove key              | `d.pop("a")`, `del d["b"]`              |
| Loop over dict          | `for k, v in d.items()`                 |
| Keys / Values / Items   | `d.keys()`, `d.values()`, `d.items()`   |
| Clear dictionary        | `d.clear()`                             |
| Dictionary comprehension| `{k: v for k, v in iterable}`           |

---

# 🎯 Tuples in Python

A **tuple** is an **ordered**, **immutable** collection. Once created, its contents cannot be changed.

---

## 🔹 Creating Tuples

```python
t1 = (1, 2, 3)
t2 = tuple(["a", "b", "c"])
t3 = (1,)  # Single-element tuple (comma required)
t4 = ()    # Empty tuple
```

---

## 🔹 Accessing Elements

```python
colors = ("red", "green", "blue")
print(colors[0])       # red
print(colors[-1])      # blue
```

---

## 🔹 Slicing Tuples

```python
t = (1, 2, 3, 4, 5)
print(t[1:4])  # (2, 3, 4)
```

---

## 🔹 Looping Through a Tuple

```python
for item in t:
    print(item)
```

---

## 🔹 Tuple Packing and Unpacking

```python
# Packing
person = ("Alice", 25, "NY")

# Unpacking
name, age, city = person
print(name, city)
```

---

## 🔹 Immutability of Tuples

```python
t = (1, 2, 3)
t[0] = 10  # ❌ Error: 'tuple' object does not support item assignment
```

---

## 🔹 When to Use Tuples?
- When data should not change (e.g., days of week)
- As keys in dictionaries (if values are immutable)
- To return multiple values from a function

---

## 🔹 Tuple Methods

```python
t = (1, 2, 2, 3, 4)
print(t.count(2))  # 2
print(t.index(3))  # 3
```

---

## 📌 Tuple Summary Table

| Operation             | Syntax                           |
|------------------------|----------------------------------|
| Create tuple           | `t = (1, 2, 3)`                  |
| Access elements        | `t[0]`, `t[-1]`                  |
| Slicing                | `t[1:3]`                         |
| Looping                | `for x in t:`                    |
| Packing/Unpacking      | `a, b = (1, 2)`                  |
| Count/Index methods    | `t.count(2)`, `t.index(3)`       |

---

## 🧪 Practice Examples

```python
# Dictionary
profile = {"name": "Zoe", "skills": ["Python", "Flask"]}
profile["location"] = "Remote"
for k, v in profile.items():
    print(f"{k}: {v}")

# Tuple
data = ("X", 100, True)
for item in data:
    print(item)

# Unpack tuple
a, b, c = data
print(a, b, c)
```
