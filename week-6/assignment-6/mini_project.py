# Pull your list copy from week-5/data/numbers.py here
numbers = [] 

def find_min(numbers):
    # Loop-based implementation (no min())
    current_min = numbers[0]
    for num in numbers:
        if num < current_min:
            current_min = num
    return current_min

def find_max(numbers):
    # Loop-based implementation (no max())
    current_max = numbers[0]
    for num in numbers:
        if num > current_max:
            current_max = num
    return current_max

def search(numbers, target):
    # Returns the index of the target, or -1 if not found
    for i in range(len(numbers)):
        if numbers[i] == target:
            return i
    return -1

def bubble_sort(numbers):
    # Returns a NEW sorted list without modifying the original
    sorted_list = numbers.copy()
    n = len(sorted_list)
    for i in range(n):
        for j in range(0, n - i - 1):
            if sorted_list[j] > sorted_list[j + 1]:
                # Swap elements
                sorted_list[j], sorted_list[j + 1] = sorted_list[j + 1], sorted_list[j]
    return sorted_list

def show_menu():
    print("\n--- Number Cruncher Menu ---")
    print("1. Find Minimum")
    print("2. Find Maximum")
    print("3. Search for a Number")
    print("4. Sort Numbers")
    print("5. Exit")
    choice = input("Choose an option (1-5): ")
    return choice

def main():
    while True:
        choice = show_menu()
        
        if choice == "1":
            minimum = find_min(numbers)
            print(f"The minimum value is: {minimum}")
            
        elif choice == "2":
            maximum = find_max(numbers)
            print(f"The maximum value is: {maximum}")
            
        elif choice == "3":
            target = int(input("Enter the number to search for: "))
            index = search(numbers, target)
            # The main() function handles printing the outcomes as required
            if index != -1:
                print(f"Found at index {index}")
            else:
                print("Not found")
                
        elif choice == "4":
            ordered_list = bubble_sort(numbers)
            print(f"Original list: {numbers}")
            print(f"Sorted list: {ordered_list}")
            
        elif choice == "5":
            print("Exiting Number Cruncher. Goodbye!")
            break
            
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
