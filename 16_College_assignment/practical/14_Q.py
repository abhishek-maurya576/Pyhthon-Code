#14.	Write a Python program to read a file line by line store it into an array.

# Ask user for the file path
file_path = input("Enter the file path: ")

try:
    with open(file_path, 'r') as file:
        lines = file.readlines()  # Read all lines into a list

    # Remove newline characters from each line (optional)
    #lines = [line.strip() for line in lines]

    print("Contents of the file as an array:")
    print(lines)

except FileNotFoundError:
    print("Error: File not found.")
