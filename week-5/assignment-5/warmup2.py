# Start an infinite loop to repeatedly ask for input until valid
while True:
    # Prompt the user to enter a positive integer
    user_input = input("Enter a positive integer: ")
    
    # Check if the input consists only of digits and is greater than zero
    if user_input.isdigit() and int(user_input) > 0:
        # Convert the verified string input into an integer
        positive_integer = int(user_input)
        # Print the success message with the valid number
        print(f"Got it: {positive_integer}")
        # Break out of the loop since a valid entry was received
        break
    else:
        # Print an error message and let the loop run again
        print("That's not a positive integer. Try again.")
