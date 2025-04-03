l = []
n,i=5,0
while i<n:
    ele = input()
    l.append(ele)
    i += 1
print(l,'\n',type(l))
tup = tuple(l)
print(tup,'\n',type(tup))
