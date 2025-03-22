# 📘 Python Conditional Statements – Complete Guide

Conditional statements in Python are used to perform different actions based on different conditions. They help you control the flow of your program.

---

## 🔹 Types of Conditional Statements

1. `if` statement
2. `if-else` statement
3. `if-elif-else` statement
4. Nested `if` statements

---

## 🔸 1. `if` Statement

Executes a block of code **only if** the condition is true.

```python
x = 10
if x > 5:
    print("x is greater than 5")
```

---

## 🔸 2. `if-else` Statement

Executes one block if the condition is true, otherwise executes the `else` block.

```python
x = 3
if x % 2 == 0:
    print("Even number")
else:
    print("Odd number")
```

---

## 🔸 3. `if-elif-else` Statement

Used for **multiple conditions**.

```python
score = 85
if score >= 90:
    print("Grade: A")
elif score >= 75:
    print("Grade: B")
elif score >= 60:
    print("Grade: C")
else:
    print("Grade: F")
```

---

## 🔸 4. Nested `if` Statements

An `if` statement inside another `if`.

```python
x = 10
y = 20

if x > 5:
    if y > 15:
        print("Both conditions are true")
```

---

## 🔸 Using Comparison and Logical Operators

You can use `==`, `!=`, `>`, `<`, `>=`, `<=`, and logical operators like `and`, `or`, `not`.

```python
age = 25
if age > 18 and age < 60:
    print("Eligible for work")
```

---

## 🔸 Using `pass` Statement

If you want a block with no action:

```python
x = 10
if x > 5:
    pass  # Do nothing (placeholder)
```

---

## 📌 Summary Table

| Statement Type     | Syntax Example                           |
|--------------------|-------------------------------------------|
| `if`               | `if x > 0:`                               |
| `if-else`          | `if x > 0: ... else: ...`                |
| `if-elif-else`     | `if ... elif ... else ...`               |
| Nested `if`        | `if x > 0: if y > 0: ...`                |
| `pass`             | `if condition: pass`                     |
| Logical Operators  | `and`, `or`, `not`                       |

---

## 🧪 Practice Examples

```python
# Example 1: Check even or odd
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")

# Example 2: Grade evaluation
marks = int(input("Enter your marks: "))
if marks >= 90:
    print("A")
elif marks >= 75:
    print("B")
elif marks >= 60:
    print("C")
else:
    print("F")
```





