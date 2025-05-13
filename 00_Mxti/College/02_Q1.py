'''Write a Python program that prompts the user to enter their year of birth. Calculate their approximate age and print a message like "You are approximately X years old." Implement basic validation: ensure the input is a valid integer representing a year (e.g., between 1900 and the current year). If the input is invalid, print an error message'''

age = input("Enter your date of birth: ")
count = 0
for x in age:
	count += 1
if count == 4:
	age = 2025 - int(age)
	print(f"You are approximately {age} year old")
else:
	print("Please enter a 4 digit valid year")