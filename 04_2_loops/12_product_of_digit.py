#Find the product of digits of a number.
num = input("Enter a number: ")
product = 1
for x in num:
    product *= int(x)
print(product)
