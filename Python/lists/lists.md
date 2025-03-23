# 📘 Python Lists – Complete Guide

A **list** in Python is a versatile and widely used built-in data structure. It allows you to store multiple items in a single variable. Lists are **ordered**, **mutable** (changeable), and can contain **duplicate values**.

---

## 🔹 Creating a List

You can create a list using square brackets `[]` or the `list()` constructor.

```python
# Using square brackets
fruits = ["apple", "banana", "cherry"]
numbers = [1, 2, 3, 4, 5]
mixed = [1, "hello", 3.14, True]

# Using list constructor
empty = list()
```

> Lists can hold any data type, and even a mix of data types.

---

## 🔹 Accessing Elements

List elements are accessed by **index**, starting at 0.

```python
fruits = ["apple", "banana", "cherry"]
print(fruits[0])   # apple
print(fruits[2])   # cherry
```

You can also use **negative indexing** to access elements from the end:

```python
print(fruits[-1])  # cherry
print(fruits[-2])  # banana
```

---

## 🔹 Modifying Elements

Lists are mutable, so you can change an element by referring to its index:

```python
fruits[1] = "blueberry"
print(fruits)  # ['apple', 'blueberry', 'cherry']
```

---

## 🔹 Adding Elements

### `append()` – Add to the end
```python
fruits.append("orange")
```

### `insert()` – Add at a specific index
```python
fruits.insert(1, "grape")
```

---

## 🔹 Removing Elements

### `remove()` – Removes by value (first match only)
```python
fruits.remove("banana")
```

### `pop()` – Removes by index (or last item by default)
```python
fruits.pop()      # last item
fruits.pop(0)     # item at index 0
```

### `clear()` – Empties the list
```python
fruits.clear()
```

---

## 🔹 List Methods

```python
my_list = [3, 1, 4, 1, 5, 9]

my_list.sort()    # Sort ascending
my_list.reverse() # Reverse order
my_list.count(1)  # Count occurrences
my_list.index(5)  # Find index of value
```

---

## 🔹 List Slicing

Get a subset of the list:

```python
numbers = [0, 1, 2, 3, 4, 5]
print(numbers[1:4])   # [1, 2, 3]
print(numbers[:3])   # [0, 1, 2]
print(numbers[3:])   # [3, 4, 5]
print(numbers[::2])  # [0, 2, 4]
```

---

## 🔹 Looping Through Lists

### Using `for` loop
```python
for fruit in fruits:
    print(fruit)
```

### Using `for` with `range()`
```python
for i in range(len(fruits)):
    print(fruits[i])
```

---

## 🔹 List Comprehension

List comprehension provides a concise way to create lists:

```python
squares = [x*x for x in range(5)]
print(squares)  # [0, 1, 4, 9, 16]
```

With condition:
```python
evens = [x for x in range(10) if x % 2 == 0]
```

---

## 🔹 Copying a List

To create a **copy** of a list (not just a reference):

```python
original = [1, 2, 3]
copy1 = original.copy()
copy2 = list(original)
copy3 = original[:]
```

> ⚠️ `copy_ref = original` only creates a reference, not a new list.

---

## 🔹 Nested Lists (2D and 3D)

### ✅ 2D Lists (Matrix)

A 2D list is a list of lists, like a table:

```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Accessing elements
print(matrix[0][0])  # 1
print(matrix[1][2])  # 6

# Loop through 2D list
for row in matrix:
    for col in row:
        print(col, end=" ")
    print()
```

### ✅ 3D Lists

A 3D list is a list of 2D lists:

```python
cube = [
    [
        [1, 2],
        [3, 4]
    ],
    [
        [5, 6],
        [7, 8]
    ]
]

# Accessing elements
print(cube[0][1][1])  # 4
print(cube[1][0][0])  # 5

# Loop through 3D list
for layer in cube:
    for row in layer:
        for item in row:
            print(item, end=" ")
        print()
    print("---")
```

> Nested lists are useful for representing matrices, grids, or multi-dimensional data structures.

---

## 🔹 Membership Testing

```python
if "apple" in fruits:
    print("Yes, apple is in the list")
```

---

## 🔹 Combining Lists

### Using `+` operator
```python
list1 = [1, 2]
list2 = [3, 4]
combined = list1 + list2
```

### Using `extend()`
```python
list1.extend(list2)
```

---

## 📌 Summary Table

| Operation            | Example                                |
|----------------------|----------------------------------------|
| Create list          | `my_list = [1, 2, 3]`                  |
| Access item          | `my_list[0]`                           |
| Modify item          | `my_list[1] = 10`                      |
| Append               | `my_list.append(4)`                    |
| Insert               | `my_list.insert(1, 'x')`               |
| Remove (by value)    | `my_list.remove('x')`                  |
| Remove (by index)    | `my_list.pop(1)`                       |
| Clear list           | `my_list.clear()`                      |
| Copy list            | `copy = my_list.copy()`                |
| Slice list           | `my_list[1:3]`                         |
| Combine lists        | `list1 + list2`                        |
| Sort list            | `my_list.sort()`                       |
| Reverse list         | `my_list.reverse()`                    |
| List comprehension   | `[x*x for x in range(5)]`              |
| Nested list access   | `matrix[1][2]`, `cube[0][1][1]`        |

---

## 🧪 Practice Examples

```python
# Create a list
languages = ["Python", "Java", "C++"]
languages.append("JavaScript")
print(languages)

# Loop and print uppercase
for lang in languages:
    print(lang.upper())

# List comprehension
squares = [x**2 for x in range(6)]
print(squares)

# Nested list example
matrix = [[1, 2], [3, 4]]
print(matrix[1][1])  # 4

# Slice and check membership
print(languages[1:3])
if "Python" in languages:
    print("Python is present!")
```




