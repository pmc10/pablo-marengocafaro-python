def is_valid_score(score):
    if isinstance(score, int) and 0 <= score <= 100:
        return True
    return False

# Ask the user for a score and convert it with int()
user_input = input("Enter a score: ")
user_score = int(user_input)

# Call your function inside an if statement
if is_valid_score(user_score):
    print("Valid score.")
else:
    print("Invalid score – must be between 0 and 100.")
