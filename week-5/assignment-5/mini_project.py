# Try to import the numbers list from the structured data path
try:
    from data.numbers import numbers
except ModuleNotFoundError:
    # Fallback list for isolated testing if the data file is missing
    numbers = [42, 7, 19, 88, 3, 25, 11]

# Main program loop to keep the interactive menu running
while True:
    print("\n=== Number Cruncher ===")
    print("1. Find minimum")
    print("2. Find maximum")
    print("3. Search for a number")
    print("4. Sort the list")
    print("5. Quit")
    
    choice = input("Choose an option (1-5): ")
    
    if choice == "1":
        # 1. Manually find the minimum value without min()
        if not numbers:
            print("The list is empty.")
        else:
            minimum_value = numbers[0]
            for num in numbers:
                if num < minimum_value:
                    minimum_value = num
            print(f"The minimum value is: {minimum_value}")
            
    elif choice == "2":
        # 2. Manually find the maximum value without max()
        if not numbers:
            print("The list is empty.")
        else:
            maximum_value = numbers[0]
            for num in numbers:
                if num > maximum_value:
                    maximum_value = num
            print(f"The maximum value is: {maximum_value}")
            
    elif choice == "3":
        # 3. Manual linear search for a target integer
        try:
            target_num = int(input("Enter a number to search for: "))
            is_found = False
            for i in range(len(numbers)):
                if numbers[i] == target_num:
                    print(f"Found {target_num} at index {i}.")
                    is_found = True
                    break
            if not is_found:
                print("Not found.")
        except ValueError:
            print("Please enter a valid integer.")
            
    elif choice == "4":
        # 4. Optimized Bubble Sort algorithm based on the lesson pseudocode
        sorted_list = list(numbers)
        list_length = len(sorted_list)
        
        while True:
            swapped = False
            # Loop through adjacent pairs up to list_length - 1 to prevent IndexError
            for i in range(0, list_length - 1):
                if sorted_list[i] > sorted_list[i + 1]:
                    # Swap the items if they are out of order
                    sorted_list[i], sorted_list[i + 1] = sorted_list[i + 1], sorted_list[i]
                    swapped = True
            
            # Exit condition: if a full pass completes without any swaps
            if not swapped:
                break
                
        print(f"Sorted list: {sorted_list}")
        
    elif choice == "5":
        # 5. Terminate the program execution
        print("Goodbye! Thanks for using Number Cruncher.")
        break
    else:
        print("Invalid option. Please choose a number between 1 and 5.")
