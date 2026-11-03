# Iterate through numbers from 1 to 30 inclusive
for i in range(1, 31):
    # Check the combined case first to prevent catching single conditions prematurely
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    # Check if the number is divisible only by 3
    elif i % 3 == 0:
        print("Fizz")
    # Check if the number is divisible only by 5
    elif i % 5 == 0:
        print("Buzz")
    # If not divisible by 3 or 5, simply print the number itself
    else:
        print(i)
