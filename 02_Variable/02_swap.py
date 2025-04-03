#Swap the values of two variables without using a third variable.
num1 = 5
num2 = 7
print("Before swapping:")
print("Value of num1 =", num1)  
print("Value of num2 =", num2)
#Swap the values of two variables without using a third variable.
num1 = num1 + num2
num2 = num1 - num2
num1 = num1 - num2
print("After swapping:")
print("Value of num1 =", num1)
print("Value of num2 =", num2)