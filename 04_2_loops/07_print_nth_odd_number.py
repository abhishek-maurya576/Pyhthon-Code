#Print the sum of all odd numbers from 1 to N.
num = int(input("Enter a number: "))
print("List Comprehension")
odd = [x for x in range(1,num+1,2)]
print(odd)
print("By loop")
for x in range(1,num+1,2):
    print(x,end=" ")
