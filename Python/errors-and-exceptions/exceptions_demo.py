# Comprehensive exception handling example

def divide_numbers():
    try:
        x = int(input("Enter numerator: "))
        y = int(input("Enter denominator: "))
        result = x / y
    except ZeroDivisionError:
        print("Cannot divide by zero!")
    except ValueError:
        print("Invalid input! Enter integers only.")
    else:
        print(f"Result is {result}")
    finally:
        print("Operation complete.")

# Raising and handling custom exceptions
class InvalidAgeError(Exception):
    def __init__(self, age):
        super().__init__(f"Invalid age: {age}")

def validate_age(age):
    if age < 0:
        raise InvalidAgeError(age)

try:
    validate_age(-2)
except InvalidAgeError as e:
    print(e)

divide_numbers()
