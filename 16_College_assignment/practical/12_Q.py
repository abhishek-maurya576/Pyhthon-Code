#Write a Python program that takes a text file as input and returns the number of words of a given text file
path = input("Enter the file path: ")
try:
    with open(path,'r') as file:
        text = file.read()
        words = text.split()
        print(f"Number of words {len(words)}")
except FileNotFoundError as e:
    print("File not found",e)
        