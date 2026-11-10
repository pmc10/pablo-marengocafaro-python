def local_scope_example():
    # 1. Define a variable inside a function
    secret_number = 42
    print("Inside the function:", secret_number)

local_scope_example()

# Attempting to access it outside the function causes a NameError:
# print(secret_number)
"""
Pasted Error:
NameError: name 'secret_number' is not defined
"""

# 2. Show how return solves the problem
def return_scope_solution():
    solved_number = 42
    return solved_number

# Assign the returned value to a variable in the outer scope
result = return_scope_solution()
print("Outside the function (solved with return):", result)
