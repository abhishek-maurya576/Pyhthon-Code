#Write a program to check whether a number is positive, negative, or zero.
print("A program to check whether a number is positive, negative, or zero.")
num = int(input("Enter a number: "))
if num>0:
    print("Number",num,"is positive")
elif num<0:
    print("Number",num,"is negative")
else:
    print("Number",num,"is zero")
