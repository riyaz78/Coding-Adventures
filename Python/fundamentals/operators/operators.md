# 📘 Python Operators – Complete Guide

Operators in Python are special symbols or keywords used to perform operations on values or variables. Python supports various types of operators such as arithmetic, comparison, logical, bitwise, assignment, identity, and membership operators.

---

## 🔹 Types of Operators

1. Arithmetic Operators
2. Comparison (Relational) Operators
3. Logical Operators
4. Assignment Operators
5. Bitwise Operators
6. Identity Operators
7. Membership Operators

---

## 🔸 1. Arithmetic Operators

Used for basic mathematical operations:

| Operator | Description       | Example        | Result  |
|----------|-------------------|----------------|---------|
| `+`      | Addition           | `5 + 3`        | `8`     |
| `-`      | Subtraction        | `5 - 2`        | `3`     |
| `*`      | Multiplication     | `4 * 2`        | `8`     |
| `/`      | Division           | `10 / 2`       | `5.0`   |
| `//`     | Floor Division     | `7 // 2`       | `3`     |
| `%`      | Modulus            | `7 % 3`        | `1`     |
| `**`     | Exponentiation     | `2 ** 3`       | `8`     |

```python
print(5 + 3)
print(10 / 2)
print(7 % 3)
```

---

## 🔸 2. Comparison Operators

Used to compare values:

| Operator | Description          | Example        | Result  |
|----------|----------------------|----------------|---------|
| `==`     | Equal to              | `5 == 5`       | `True`  |
| `!=`     | Not equal to          | `5 != 3`       | `True`  |
| `>`      | Greater than          | `7 > 5`        | `True`  |
| `<`      | Less than             | `4 < 6`        | `True`  |
| `>=`     | Greater than or equal| `7 >= 7`       | `True`  |
| `<=`     | Less than or equal   | `5 <= 5`       | `True`  |

```python
x = 10
y = 20
print(x == y)
print(x < y)
```

---

## 🔸 3. Logical Operators

Used to combine conditional statements:

| Operator | Description         | Example                 | Result  |
|----------|---------------------|--------------------------|---------|
| `and`    | Logical AND         | `True and False`         | `False` |
| `or`     | Logical OR          | `True or False`          | `True`  |
| `not`    | Logical NOT         | `not True`               | `False` |

```python
x = 5
y = 10
print(x > 2 and y > 5)
print(x < 3 or y < 15)
```

---

## 🔸 4. Assignment Operators

Used to assign values to variables:

| Operator | Example  | Equivalent To  |
|----------|----------|----------------|
| `=`      | `x = 5`  | Assign 5 to x  |
| `+=`     | `x += 3` | `x = x + 3`    |
| `-=`     | `x -= 2` | `x = x - 2`    |
| `*=`     | `x *= 4` | `x = x * 4`    |
| `/=`     | `x /= 2` | `x = x / 2`    |
| `%=`     | `x %= 3` | `x = x % 3`    |
| `//=`    | `x //= 2`| `x = x // 2`   |
| `**=`    | `x **= 2`| `x = x ** 2`   |

```python
x = 5
x += 3
print(x)
```

---

## 🔸 5. Bitwise Operators

Bitwise operators perform operations at the **bit level** of integer values.

| Operator | Description | Example     | Result |
|----------|-------------|-------------|--------|
| `&`      | AND         | `5 & 3`     | `1`    |
| `|`      | OR          | `5 | 3`     | `7`    |
| `^`      | XOR         | `5 ^ 3`     | `6`    |
| `~`      | NOT         | `~5`        | `-6`   |
| `<<`     | Left Shift  | `2 << 1`    | `4`    |
| `>>`     | Right Shift | `4 >> 1`    | `2`    |

### 👉 How it works :
- **Binary**: All numbers are converted to binary.
- `&` (AND) returns 1 only if both bits are 1.
- `|` (OR) returns 1 if at least one bit is 1.
- `^` (XOR) returns 1 if bits differ.
- `~` inverts bits (also flips the sign in 2's complement).
- `<<` shifts bits left (multiplies by 2).
- `>>` shifts bits right (divides by 2).

```python
print(5 & 3)   # 1
print(~5)      # -6
print(2 << 1)  # 4
```

---

## 🔸 6. Identity Operators

Used to compare memory locations:

| Operator | Description             | Example           | Result |
|----------|-------------------------|-------------------|--------|
| `is`     | Same object              | `x is y`          | `True/False` |
| `is not` | Not same object         | `x is not y`      | `True/False` |

```python
a = [1, 2]
b = a
c = [1, 2]
print(a is b)      # True
print(a is c)      # False
```

---

## 🔸 7. Membership Operators

Used to check if a value exists in a sequence:

| Operator | Description      | Example         | Result |
|----------|------------------|------------------|--------|
| `in`     | Value exists      | `'a' in 'cat'`   | `True` |
| `not in` | Value does not exist | `'x' not in 'cat'` | `True` |

```python
print('a' in 'apple')
print('x' not in 'banana')
```

---

