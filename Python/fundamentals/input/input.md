# 📘 Python `input()` Function – Complete Guide

The `input()` function in Python is used to **take input from the user** through the console. It pauses program execution until the user types something and presses Enter.

---

## 🔹 Basic Syntax

```python
input([prompt])
```

- **`prompt`** *(optional)*: A string that is displayed to the user before taking input.
- The return value is always of **string** type.

---

## 🔸 Basic Example

```python
name = input("Enter your name: ")
print("Hello,", name)
```

**Output:**
```
Enter your name: Alice
Hello, Alice
```

---

## 🔸 Type Conversion (Casting)

Since input is always returned as a string, you must convert it if you need numeric types:

```python
age = input("Enter your age: ")
print(type(age))  # <class 'str'>

age = int(age)
print(type(age))  # <class 'int'>
```

### Shortcut:
```python
age = int(input("Enter your age: "))
```

---

## 🔸 Handling Multiple Inputs

You can use `.split()` to read multiple values in one line:

```python
a, b = input("Enter two numbers: ").split()
print("a =", a)
print("b =", b)
```

### With type casting:
```python
a, b = map(int, input("Enter two integers: ").split())
```

---

## 🔸 Using `input()` in Loops

```python
for i in range(3):
    val = input(f"Enter value {i+1}: ")
    print("You entered:", val)
```

---

## 🔸 Common Mistakes

❌ Forgetting to convert input:
```python
x = input("Enter a number: ")
print(x + 5)  # Error: cannot add string and int
```

✅ Correct:
```python
x = int(input("Enter a number: "))
print(x + 5)
```

---

## 📌 Summary Table

| Feature                | Description                                |
|------------------------|--------------------------------------------|
| Basic Input            | `name = input()`                           |
| With Prompt            | `name = input("Enter your name:")`        |
| Type Conversion        | `int(input())`, `float(input())`           |
| Multiple Inputs        | `a, b = input().split()`                   |
| Map with Type Casting  | `map(int, input().split())`                |

---

## 🧪 Practice Examples

```python
# Basic input
username = input("What's your name? ")
print("Welcome,", username)

# Integer input
age = int(input("Enter your age: "))
print("You will be", age + 1, "next year.")

# Multiple values
x, y = map(float, input("Enter two decimals: ").split())
print("Sum =", x + y)
```

---

