# 🔤 Python String Methods – Complete Guide

Strings are one of the most commonly used data types in Python. Python provides numerous built-in string methods to manipulate and work with strings efficiently.

---

## 📌 What is a String in Python?
A **string** is a sequence of characters enclosed in quotes (`' '` or " ").

```python
my_string = "Hello, Python!"
print(my_string)  # Output: Hello, Python!
```

---

## 🔹 Common String Methods

### 1️⃣ Changing Case

#### `upper()` – Converts a string to uppercase
```python
text = "hello world"
print(text.upper())  # Output: HELLO WORLD
```

#### `lower()` – Converts a string to lowercase
```python
text = "HELLO WORLD"
print(text.lower())  # Output: hello world
```

#### `title()` – Converts the first letter of each word to uppercase
```python
text = "hello python world"
print(text.title())  # Output: Hello Python World
```

#### `capitalize()` – Capitalizes the first character of the string
```python
text = "python programming"
print(text.capitalize())  # Output: Python programming
```

---

### 2️⃣ Checking String Content

#### `startswith()` – Checks if a string starts with a specific substring
```python
text = "Python is amazing"
print(text.startswith("Python"))  # Output: True
```

#### `endswith()` – Checks if a string ends with a specific substring
```python
text = "data.csv"
print(text.endswith(".csv"))  # Output: True
```

#### `isalpha()` – Returns `True` if all characters are alphabets
```python
text = "Python"
print(text.isalpha())  # Output: True
```

#### `isdigit()` – Returns `True` if all characters are digits
```python
text = "12345"
print(text.isdigit())  # Output: True
```

#### `isalnum()` – Returns `True` if all characters are alphanumeric
```python
text = "Python123"
print(text.isalnum())  # Output: True
```

---

### 3️⃣ Finding & Replacing Substrings

#### `find()` – Returns the first occurrence index of a substring
```python
text = "Python is fun"
print(text.find("fun"))  # Output: 10
```

#### `replace()` – Replaces occurrences of a substring
```python
text = "I love Java"
print(text.replace("Java", "Python"))  # Output: I love Python
```

---

### 4️⃣ Splitting & Joining Strings

#### `split()` – Splits a string into a list based on a separator
```python
text = "apple,banana,grape"
print(text.split(","))  # Output: ['apple', 'banana', 'grape']
```

#### `join()` – Joins elements of an iterable into a string
```python
words = ["Python", "is", "awesome"]
print(" ".join(words))  # Output: Python is awesome
```

---

### 5️⃣ Stripping Whitespace

#### `strip()` – Removes leading and trailing whitespace
```python
text = "  Hello, Python!  "
print(text.strip())  # Output: Hello, Python!
```

#### `lstrip()` – Removes leading whitespace
```python
text = "  Hello"
print(text.lstrip())  # Output: Hello
```

#### `rstrip()` – Removes trailing whitespace
```python
text = "Hello  "
print(text.rstrip())  # Output: Hello
```

---

## 🔥 Summary Table

| Method       | Description |
|-------------|-------------------------------------------------|
| `upper()`   | Converts string to uppercase |
| `lower()`   | Converts string to lowercase |
| `title()`   | Capitalizes first letter of each word |
| `capitalize()` | Capitalizes the first letter of the string |
| `startswith()` | Checks if string starts with a given substring |
| `endswith()` | Checks if string ends with a given substring |
| `isalpha()` | Checks if all characters are alphabets |
| `isdigit()` | Checks if all characters are digits |
| `isalnum()` | Checks if all characters are alphanumeric |
| `find()` | Finds the index of a substring |
| `replace()` | Replaces occurrences of a substring |
| `split()` | Splits a string into a list |
| `join()` | Joins a list into a string |
| `strip()` | Removes leading and trailing whitespace |
| `lstrip()` | Removes leading whitespace |
| `rstrip()` | Removes trailing whitespace |

---

### 🎯 Final Example: Using Multiple String Methods Together
```python
text = "   python programming is fun!   "
formatted_text = text.strip().capitalize().replace("fun", "awesome")
print(formatted_text)  # Output: Python programming is awesome!
```

