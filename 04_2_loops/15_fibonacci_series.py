# Generate the Fibonacci series up to N terms.
num = int(input("Enter a number: "))
a,b = 0,1
print(a,b,end=" ")
for x in range(num-2):
    nextterm = a+b
    print(nextterm,end = " ")
    a = b
    b = nextterm
    
