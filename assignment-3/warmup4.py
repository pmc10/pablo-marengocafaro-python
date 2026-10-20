# Ask the user for a number
user_input = input("Enter a number: ")
number = int(user_input)

# Block 1: Check sign (positive, negative, or zero)
if number > 0:
    print(f"{number} is positive.")
elif number < 0:
    print(f"{number} is negative.")
else:
    print(f"{number} is zero.")

# Block 2: Check parity (even or odd)
if number % 2 == 0:
    print(f"{number} is even.")
else:
    print(f"{number} is odd.")
