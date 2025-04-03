#write a program to find greater of three given numbers using functions. pass the numbers as argument
num1=int(input('Enter number: '))
num2=int(input('Enter number: '))
num3=int(input('Enter number: '))
def great(a,b,c):
    if a>b and a>c:
        print(a,'is greater than',b,'and',c)
    elif b>a and b>c:
        print(b,'is greater than',a,'and',c)
    else:
        print('%d is greater'%c)
great(num1,num2,num3)
