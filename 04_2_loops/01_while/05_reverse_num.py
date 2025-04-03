#Build a program to reverse a number using a while loop.
num = int(input("Enter a number: "))
print("You entered number is: ",num)
i = 1
while i<=num:
    x = num%10
    i += 1
print(x)
