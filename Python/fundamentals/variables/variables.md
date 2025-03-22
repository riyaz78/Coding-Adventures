# 📘 Python Variables – Complete Guide

In Python, **variables** are used to store data. They act as containers or names for values in memory. You can think of them as labels attached to data so you can reuse and manipulate it.

---

## 🔹 Creating Variables

In Python, you don't need to declare the type of variable. It is **dynamically typed**.

```python
x = 10
name = "Alice"
pi = 3.14
```

Here,
- `x` is an integer
- `name` is a string
- `pi` is a float

---

## 🔹 Variable Naming Rules

- Names can include letters, numbers, and underscores.
- Must start with a letter or underscore (`_`), not a number.
- Case-sensitive (`age`, `Age`, and `AGE` are different).

✅ Valid:
```python
name = "Bob"
_age = 25
user2 = "Alice"
```

❌ Invalid:
```python
2user = "John"   # Starts with a number
user-name = "Eve" # Hyphens are not allowed
```

---

## 🔹 Multiple Assignments

You can assign values to multiple variables at once:

```python
a, b, c = 1, 2, 3
print(a, b, c)
```

Or assign one value to multiple variables:

```python
x = y = z = 100
```

---

## 🔹 Variable Types

Python automatically detects the data type:

```python
x = 5           # int
y = 3.14        # float
name = "Alice" # str
is_valid = True # bool
```

You can check the type using `type()`:

```python
print(type(x))
print(type(name))
```

---

## 🔹 Constants

Python doesn’t have true constants, but by convention, variables written in all uppercase are treated as constants:

```python
PI = 3.14159
MAX_USERS = 100
```

They can still be changed, but shouldn’t be.

---

## 🔹 Type Casting

Convert one type to another:

```python
x = 5
print(float(x))  # 5.0

s = "123"
print(int(s))    # 123
```

---

## 🔹 Deleting Variables

You can delete a variable using `del`:

```python
x = 10
del x
# print(x)  # This will raise an error
```

---

## 📌 Summary Table

| Feature                | Example                         |
|------------------------|---------------------------------|
| Variable Declaration   | `x = 10`                        |
| Multiple Assignment    | `a, b = 1, 2`                   |
| Same Value Assignment  | `x = y = z = 100`               |
| Type Checking          | `type(x)`                       |
| Constant Convention    | `PI = 3.14`                     |
| Type Conversion        | `int("5")`, `str(10)`           |
| Deleting Variable      | `del x`                         |

---

