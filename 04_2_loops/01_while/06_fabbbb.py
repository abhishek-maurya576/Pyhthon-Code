#Create a program that generates the first n Fibonacci numbers using a loop.
num = int(input("Enter a number: "))
t1,t2 = 0,1
print(t1,t2,end=" ")
i = 3
while i<=num:
    nextterm = t1+t2
    print(nextterm,end=" ")
    t1 = t2
    t2 = nextterm
    i += 1
