#factorial
num = int(input("Enter a number: "))
def fact(x):
    if x == 0:
        return 1
    else:
        return x*fact(x-1)
print("Factorial: ",fact(num))
