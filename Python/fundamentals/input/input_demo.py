# Simple input
name = input("Enter your name: ")
print("Hello,", name)

# Input with type casting
age = int(input("Enter your age: "))
print("Age next year:", age + 1)

# Multiple inputs
a, b = map(int, input("Enter two integers: ").split())
print("Sum:", a + b)