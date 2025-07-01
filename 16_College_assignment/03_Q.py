# Q 03. Write a Python function that takes a number as input from the user and prints its multiplication table.
def print_multiplication_table():
    try:
        number = int(input("Enter a number to print its multiplication table: "))
        print(f"\nMultiplication Table for {number}:\n")
        for i in range(1, 11):
            print(f"{number} x {i} = {number * i}")
    except ValueError:
        print("Invalid input. Please enter an integer.")

# Call the function
print_multiplication_table()
