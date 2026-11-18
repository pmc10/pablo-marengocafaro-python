import csv
import os
from datetime import datetime

# Build the file path safely
file_path = os.path.join("..", "data", "expenses.csv")

# 1. Verify that ../data/expenses.csv exists before opening it
if not os.path.exists(file_path):
    print("Error: ../data/expenses.csv not found.")
    exit()

# 2. Read ../data/expenses.csv into a list of dictionaries using csv.DictReader
expenses = []
with open(file_path, "r", newline="") as file:
    reader = csv.DictReader(file)
    for row in reader:
        # 3. Convert the amount field to float for each row
        row["amount"] = float(row["amount"])
        expenses.append(row)

# 4. Filter the list to only rows where category is "Food"
food_expenses = [row for row in expenses if row["category"] == "Food"]

# 5. Calculate the total amount spent on Food
total_food = sum(row["amount"] for row in food_expenses)

# Format today's date as "Month DD, YYYY"
today_str = datetime.now().strftime("%B %d, %Y")

# 6. Write the report to food_report.txt
with open("food_report.txt", "w") as report:
    report.write(f"Food Expense Report - generated {today_str}\n")
    for item in food_expenses:
        report.write(f"{item['date']}: ${item['amount']:.2f}\n")
    report.write(f"Total: ${total_food:.2f}\n")

print("food_report.txt generated successfully.")
