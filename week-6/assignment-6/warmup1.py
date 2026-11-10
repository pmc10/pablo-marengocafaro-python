def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

# 1. Call it with only a name argument
greet("Alex")

# 2. Call it with both a name and a custom greeting
greet("Alex", "Good morning")

# 3. Call it with the greeting passed as a keyword argument
greet("Alex", greeting="Hello")
