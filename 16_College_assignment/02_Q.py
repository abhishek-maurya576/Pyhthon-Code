l1 = []
l2 = []
l3 = []
num = int(input("Enter a list element number: "))
i = 0
while i<num:
    print("Enter first list element at index ",i+1,end = ": ")
    temp1 = int(input())
    l1.append(temp1)
    print("Enter second list element at index ",i+1,end = ": ")
    temp2 = int(input())
    l2.append(temp2)
    i += 1
for x in (l1,l2):
    sum = x 
    l3.append(sum)
print(l3)
