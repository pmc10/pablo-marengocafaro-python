# Ask user for age and convert it to an integer
age_input = input("Enter your age: ")
age = int(age_input)

# Check age ranges using conditional structures and boolean operators
if age >= 0 and age <= 12:
    print("You are a Child.")
elif age >= 13 and age <= 17:
    print("You are a Teen.")
elif age >= 18 and age <= 64:
    print("You are an Adult.")
elif age >= 65:
    print("You are a Senior.")
else:
    print("Invalid age entered.")
