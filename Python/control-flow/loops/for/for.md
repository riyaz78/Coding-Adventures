# 📘 Python `for` Loop – Complete Guide

The `for` loop in Python is used to iterate over a **sequence** (like a list, tuple, dictionary, set, or string). It allows you to run a block of code multiple times with a different value each time.

---

## 🔹 Syntax

```python
for variable in sequence:
    # block of code
```

- `variable` takes the value of each item in the sequence.
- The loop continues until all items are exhausted.

---

## 🔸 Basic Example

```python
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
```

**Output:**
```
apple
banana
cherry
```

---

## 🔸 Using `range()` with `for`

The `range()` function is commonly used to loop over a sequence of numbers:

```python
for i in range(5):
    print(i)
```

**Output:**
```
0
1
2
3
4
```

---

### `range(start, stop, step)`

```python
for i in range(1, 10, 2):
    print(i)
```

**Output:**
```
1
3
5
7
9
```

---

## 🔸 Looping through Strings

```python
for char in "Python":
    print(char)
```

**Output:**
```
P
y
t
h
o
n
```

---

## 🔸 Looping through Dictionaries

```python
person = {"name": "Alice", "age": 30}
for key in person:
    print(key, "=", person[key])
```

---

## 🔸 Nested `for` Loops

A loop inside another loop:

```python
for i in range(3):
    for j in range(2):
        print(i, j)
```

---

## 🔸 Using `break` and `continue`

```python
# break example
for num in range(10):
    if num == 5:
        break
    print(num)

# continue example
for num in range(5):
    if num == 2:
        continue
    print(num)
```

---

## 🔸 Using `else` with `for`

```python
for i in range(3):
    print(i)
else:
    print("Loop completed")
```

The `else` block runs **after the loop finishes**, unless a `break` occurs.

---

## 📌 Summary Table

| Feature         | Description                                       |
|----------------|---------------------------------------------------|
| `for`          | Iterate over elements in a sequence               |
| `range()`      | Generate a sequence of numbers                    |
| `break`        | Exit loop early                                   |
| `continue`     | Skip current iteration                           |
| `else`         | Executes after loop unless `break` is hit        |
| Nested Loops   | Loop inside another loop                          |

---

## 🧪 Practice Examples

```python
# Print numbers from 1 to 5
for i in range(1, 6):
    print(i)

# Loop through characters
for ch in "hello":
    print(ch)

# Print only even numbers from 1 to 10
for num in range(1, 11):
    if num % 2 == 0:
        print(num)

# Nested loop
for x in range(1, 4):
    for y in range(1, 3):
        print(f"x={x}, y={y}")
```






