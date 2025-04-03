num1 = int(input("Enter a first number: ")) #5
num2 = int(input("Enter a second number: ")) #7
swap = num1+num2
num1 = swap - num1
num2 = swap - num2
print("First number after swapping: ", num1) #7
print("Second number after swapping: ", num2) #5
num1 = num1+num2
num2 = num1-num2
num1 = num1 - num2
print("num1: ",num1)
print("num2: ",num2)