num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print(f"/nBefore swapping\nFirst Number: {num1}\nSecond number: {num2}")
num1,num2 = num2,num1
print(f"\nAfter swapping\nFirst Number: {num1}\nSecond number: {num2}")