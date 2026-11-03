# Predefined list of names for the search operation
names = ["Alice", "Bob", "Charlie", "Marcus", "Emily", "David"]

# Ask the user for the target name they want to locate
target_name = input("Enter a name to search for: ")

# Initialize tracking variables to monitor search state
is_found = False
found_index = -1

# Loop through the list manually using indices to avoid .index() or 'in' operator
for i in range(len(names)):
    # Check if the current element matches the target name
    if names[i] == target_name:
        is_found = True
        found_index = i
        # Stop the loop immediately once the first match is found
        break

# Display the outcome based on whether the name was located or not
if is_found:
    print(f'Found "{target_name}" at index {found_index}.')
else:
    print(f'"{target_name}" was not found in the list.')
