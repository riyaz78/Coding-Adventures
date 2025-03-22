# Simple while loop
n = 1
while n <= 3:
    print("n =", n)
    n += 1

# while with break
count = 0
while True:
    if count == 5:
        break
    print("Inside loop, count =", count)
    count += 1

# while with continue
x = 0
while x < 5:
    x += 1
    if x == 2:
        continue
    print("x =", x)