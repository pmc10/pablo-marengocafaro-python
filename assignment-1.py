# Section 1
title = "Profile Card"
birth_year = 2030
desired_grade = 9.5
likes_python = True

print(title, "is of type:", type(title))
print(birth_year, "is of type:", type(birth_year))
print(desired_grade, "is of type:", type(desired_grade))
print(likes_python, "is of type:", type(likes_python))

print("-" * 40)

# Section 2
username = input("Enter your name: ")
birth_year_input = int(input("Enter your birth year: "))
calculated_age = 2026 - birth_year_input

print(f"Hi, {username}! You are approximately {calculated_age} years old.")
print("-" * 40)

# Section 3
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
product = num1 * num2

print(f"{num1} x {num2} = {product}")
print("-" * 40)

# Section 4
item = "Notebook Pro"
price = 899.99
quantity = 2
receipt_total = price * quantity

print("==============================")
print("           RECEIPT            ")
print("==============================")
print(f"Item: {item}")
print(f"Price: ${price}")
print(f"Quantity: {quantity}")
print("------------------------------")
print(f"Total: ${receipt_total:.2f}")
print("==============================")
print("-" * 40)

# Section 5
profile_name = input("Your name: ")
profile_hometown = input("Your hometown: ")
profile_hobby = input("Your favorite hobby: ")
profile_fun_fact = input("A fun fact about yourself: ")
profile_birth_year = int(input("Birth year: "))
profile_age = 2026 - profile_birth_year

print("\n" + "="*40)
print(f"           PROFILE: {profile_name}")
print("="*40)
print(f"Hometown: {profile_hometown}")
print(f"Hobby: {profile_hobby}")
print(f"Fun fact: {profile_fun_fact}")
print(f"Age: {profile_age}")
print("="*40)
