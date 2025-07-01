"""
Q4. Write a Python program that:

1. Takes the name of a file as input from the user.

2. Asks the user to enter the number of lines they want to write.

3. Accepts text input for the specified number of lines and writes the content to the given file.

"""
def write_to_file():
    # Step 1: Take file name as input
    file_name = input("Enter the file name (with extension, e.g., example.txt): ")

    try:
        # Step 2: Take number of lines as input
        num_lines = int(input("Enter the number of lines you want to write: "))

        # Step 3: Open the file in write mode
        with open(file_name, 'w') as file:
            print(f"Enter {num_lines} line(s) of text:")
            for i in range(1, num_lines + 1):
                line = input(f"Line {i}: ")
                file.write(line + '\n')

        print(f"\nContent successfully written to '{file_name}'.")
        
    except ValueError:
        print("Invalid input. Please enter a valid number for lines.")

# Call the function
write_to_file()
