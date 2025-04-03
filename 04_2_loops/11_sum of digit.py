#Find the sum of digits of a number (e.g., 123 → 1+2+3=6).
num = input("Enter a number: ")
sum = 0
for x in num:
    sum += int(x)
print(sum)
