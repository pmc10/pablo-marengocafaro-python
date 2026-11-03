# Hardcoded student dictionary
student = {
    "name": "Carlos",
    "grade": 85,
    "subjects": ["Python", "Data", "Web"]
}

# 1. Print each key-value pair using .items() in a for loop
for key, value in student.items():
    print(f"{key}: {value}")

# 2. Add a new key "graduated" with the value False
student["graduated"] = False

# 3. Print the updated dictionary
print("\nUpdated dictionary:")
print(student)
