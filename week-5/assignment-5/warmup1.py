# Initialize the accumulator variable to hold the total sum
total_sum = 0

# Loop through numbers from 1 to 100 (range stops at 101 because the upper bound is exclusive)
for number in range(1, 101):
    # Add the current number to the running total
    total_sum += number

# Print the final result matching the requested output format
print(f"The sum of 1 to 100 is {total_sum}.")
