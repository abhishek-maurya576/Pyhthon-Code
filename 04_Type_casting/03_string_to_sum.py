#Take a list of numbers as a string, split it, and convert each element into integers for calculation (e.g., summing them up).
num = input("Enter a number: ")
sum = 0
i = 0
while i<num:
    i = int(num[i])
    sum += i
print("Total sum: ",sum)
