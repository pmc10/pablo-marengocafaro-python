import os

# 1. Print current working directory
print(os.getcwd())

# 2. Check whether ../data/expenses.csv exists
if os.path.exists("../data/expenses.csv"):
    print("expenses.csv found.")
else:
    print("expenses.csv not found.")

# 3. Build and print the path using os.path.join()
file_path = os.path.join("..", "data", "expenses.csv")
print(file_path)
