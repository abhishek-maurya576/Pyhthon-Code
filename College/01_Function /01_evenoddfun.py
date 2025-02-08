le=[]
lo=[]
num=int(input("Enter a natural num: "))

def oddeven(n):
    i=1
    while i<=n:
        if i%2==0:
            le.append(i)
        else:
            lo.append(i)
        i+=1
oddeven(num)
print("Even: ",le,"\nTotal sum: ",sum(le))
print("Odd: ",lo,"\nTotal sum: ",sum(lo))
