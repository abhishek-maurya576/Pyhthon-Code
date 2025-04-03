#write a program to find greater of three given numbers using functions. pass the numbers as argument
num1=int(input('Enter number: '))
num2=int(input('Enter number: '))
num3=int(input('Enter number: '))
def great(a,b,c):
    if a>b and a>c:
        return a
    elif b>a and b>c:
        return b
    else:
        return c
print('Greatest Number is:',great(num1,num2,num3))
