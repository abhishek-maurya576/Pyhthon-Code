# Check if a number is prime or not.
num = int(input("Enter a number: "))
isprime = 0
isnotprime = 0
i = 1
while i<=num:
    if num%i != 0:
        isprime = 1
    else:
        isnotprime = 1
    i += 1
if isprime == 1:
    print("Num %d is prime"%num)
if isnotprime == 1:
    print("Num %d is not prime"%num)
