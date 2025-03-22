# 📘 Python `while` Loop – Complete Guide

The `while` loop in Python is used to execute a block of code **repeatedly** as long as a given condition is `True`. It is one of the most fundamental loops used for iteration.

---

## 🔹 Syntax

```python
while condition:
    # block of code
```

- The `condition` is evaluated before each iteration.
- If it is `True`, the loop continues. If `False`, the loop ends.

---

## 🔸 Basic Example

```python
count = 1
while count <= 5:
    print("Count is:", count)
    count += 1
```

**Output:**
```
Count is: 1
Count is: 2
Count is: 3
Count is: 4
Count is: 5
```

---

## 🔸 Infinite Loop

A loop that never ends unless externally interrupted:

```python
while True:
    print("This runs forever! Use Ctrl+C to stop.")
```

> ⚠️ Be careful with infinite loops! Always make sure there is an exit condition.

---

## 🔸 Using `break` Statement

`break` is used to **exit** the loop prematurely:

```python
while True:
    name = input("Enter 'exit' to quit: ")
    if name == 'exit':
        break
    print("Hello,", name)
```

---

## 🔸 Using `continue` Statement

`continue` skips the current iteration and moves to the next:

```python
x = 0
while x < 5:
    x += 1
    if x == 3:
        continue
    print(x)
```

**Output:**
```
1
2
4
5
```

---

## 🔸 Using `else` with `while`

The `else` block is executed **only if the loop wasn't terminated by `break`**.

```python
x = 0
while x < 3:
    print(x)
    x += 1
else:
    print("Loop finished")
```

---

## 📌 Summary Table

| Keyword     | Description                                      |
|-------------|--------------------------------------------------|
| `while`     | Executes as long as condition is `True`          |
| `break`     | Exits the loop completely                        |
| `continue`  | Skips the current iteration                      |
| `else`      | Executes if loop finishes naturally              |

---

## 🧪 Practice Examples

```python
# Countdown
x = 5
while x > 0:
    print(x)
    x -= 1

# Skip even numbers
i = 0
while i < 10:
    i += 1
    if i % 2 == 0:
        continue
    print(i)

# Password checker
while True:
    pwd = input("Enter password: ")
    if pwd == "secret":
        print("Access granted!")
        break
    else:
        print("Try again.")
```



