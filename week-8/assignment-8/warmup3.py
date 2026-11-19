file_path = "../data/missing.txt"

try:
    with open(file_path, "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print('Error: "missing.txt" was not found. Please check the file path and try again.')
