#Find the factorial of a given number.
num = int(input("Enter a number: "))
i = 0
while i<num:
    if num == 0:
        print("factorial : %d"%num)
    else:
        fact = num*(num-1)
        num -= 1
    i += 1
print(fact)
