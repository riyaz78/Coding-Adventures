def string_operations():
    text = "  Hello, Python World!  "
    print("Original String:", text)
    
    # Case Modifications
    print("Uppercase:", text.upper())
    print("Lowercase:", text.lower())
    print("Title Case:", text.title())
    print("Capitalized:", text.capitalize())
    print("Swapcase:", text.swapcase())
    
    # Trimming and Alignment
    print("Stripped:", text.strip())
    print("Left Stripped:", text.lstrip())
    print("Right Stripped:", text.rstrip())
    
    # Searching
    print("Index of 'Python':", text.find("Python"))
    print("Starts with 'Hello':", text.startswith("Hello"))
    print("Ends with 'World!':", text.endswith("World!"))
    
    # Replacing
    new_text = text.replace("Python", "Coding")
    print("Replaced String:", new_text)
    
    # Splitting & Joining
    words = text.split(" ")
    print("Split Words:", words)
    print("Joined Words:", "-".join(words))
    
    # Checking Types
    print("Is Alphabetic?", "Python".isalpha())
    print("Is Numeric?", "1234".isdigit())
    print("Is Alphanumeric?", "Python123".isalnum())
    
    # Formatting
    age = 30
    print(f"Formatted: My age is {age} years.")

# Run the function
string_operations()