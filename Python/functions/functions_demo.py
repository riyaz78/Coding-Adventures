def greet(name):
    print(f"Hello, {name}!")

def add(x, y):
    return x + y

def describe_pet(animal="dog", name="Buddy"):
    print(f"I have a {animal} named {name}.")

def display_args(*args):
    for a in args:
        print(a)

def display_kwargs(**kwargs):
    for k, v in kwargs.items():
        print(f"{k} = {v}")

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

# Lambda
square = lambda x: x * x

# Calls
greet("Alice")
print(add(10, 20))
describe_pet(name="Charlie", animal="parrot")
display_args(1, 2, 3)
display_kwargs(city="NYC", age=25)
print(factorial(5))
print(square(6))


