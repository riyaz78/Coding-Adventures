# Creating a dictionary with key-value pairs
student = {
    "name": "John",
    "age": 20,
    "grade": "A",
    "subjects": ["Math", "Science", "History"]
}

# Accessing values
print("Name:", student["name"])
print("Subjects:", student.get("subjects"))

# Adding and modifying entries
student["school"] = "Springfield High"
student["grade"] = "A+"

# Removing an entry
student.pop("age")

# Looping through dictionary
print("\nStudent Profile:")
for key, value in student.items():
    print(f"{key}: {value}")

# Dictionary comprehension
squares = {x: x ** 2 for x in range(1, 6)}
print("\nSquares Dictionary:", squares)

# Nested dictionary example
school = {
    "class1": {"teacher": "Mr. Smith", "students": 30},
    "class2": {"teacher": "Ms. Lee", "students": 28}
}
print("\nClass 1 Teacher:", school["class1"]["teacher"])