# List basics
numbers = [1, 2, 3, 4, 5]
print(numbers[0])
numbers.append(6)
print(numbers)

# Modifying list
numbers[2] = 100
print(numbers)

# Looping
for n in numbers:
    print(n)

# List comprehension
even = [x for x in numbers if x % 2 == 0]
print("Even numbers:", even)

# Copy and combine
copy = numbers.copy()
combined = numbers + [7, 8]
print("Combined:", combined)

# Nested lists
matrix = [[1, 2], [3, 4]]
print(matrix[0][1])  # 2

# 3D list
cube = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]
print(cube[1][0][1])  # 6


