# Creating tuples
t1 = (10, 20, 30)
t2 = tuple(["a", "b", "c"])
t3 = (1,)  # single element tuple

# Accessing tuple elements
print("First element of t1:", t1[0])
print("Last element of t2:", t2[-1])

# Slicing
print("Slice of t1:", t1[1:])

# Tuple packing and unpacking
info = ("Alice", 25, "NY")
name, age, city = info
print(f"Name: {name}, City: {city}")

# Looping
print("\nLooping through t2:")
for item in t2:
    print(item)

# Immutability
try:
    t1[0] = 100  # This will raise an error
except TypeError as e:
    print("Error:", e)

# Tuple methods
t = (1, 2, 2, 3, 4)
print("Count of 2:", t.count(2))
print("Index of 3:", t.index(3))