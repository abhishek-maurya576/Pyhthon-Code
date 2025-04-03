#wap to create a list of 5 element print element
lst = [2,5,4,8,'Hey']
print(lst)
print("\nIn next line")
for x in lst:
    print(x)

print("\nIn one line string class")
typ = 5
for x in lst:
    print(x,end = ' ')
    typ = x
print(type(typ))
print('\nBy while loop')
i = 0
while i < len(lst):
    print(lst[i])
    i += 1
    
print('\nBy while loop with -ve indexing and assecing from last index')
i = -1
while i >= -len(lst):
    print(lst[i])
    i -= 1
    
