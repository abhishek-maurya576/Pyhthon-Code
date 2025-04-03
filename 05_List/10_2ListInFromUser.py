#add corresponding list element
l1 = []
l2 = []
sumList = []
sum = 0
n = int(input("Enter list capacity: "))
i = 0
#list1
print("Enter first List element")
while (i<n) :
    l1.append(int(input()))
    i += 1
#list2
j = 0
print("Enter second List element")
while (j<n):
    l2.append(int(input()))
    j += 1
print("List 1: ",l1)
print("List 2: ",l2)
for x,y in zip(l1,l2) :
    sumList.append(x+y)
print("Sum: ",sumList)