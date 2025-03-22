# Loop through a list
colors = ["red", "green", "blue"]
for color in colors:
    print(color)

# Loop using range
for i in range(5):
    print("i =", i)

# Nested for loop
for i in range(2):
    for j in range(2):
        print(i, j)

# Loop with break
for i in range(5):
    if i == 3:
        break
    print("Break example:", i)

# Loop with continue
for i in range(5):
    if i == 2:
        continue
    print("Continue example:", i)
