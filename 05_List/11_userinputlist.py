l = []
n = int(input("Enter a List item: "))
r = 0
while r<n:
    a = input("Enter element you want to store\nEnter int = Integer\tfloat = Floatin value\tstr = String")
    if a == 'int' or 'INT' or 'Int':
        x = int(input("Enter a interger value: "))
        l.append(x)
    a = input("Enter element you want to store\nEnter int = Integer\tfloat = Floatin value\tstr = String")
    elif a == 'float' or 'FLOAT' or 'Float':
        x = float(input("Enter a interger value: "))
        l.append(x)
    a = input("Enter element you want to store\nEnter int = Integer\tfloat = Floatin value\tstr = String")
    elifa == 'str' or 'STR' or 'Str':
        x = input("Enter a interger value: ")
        l.append(x)
    a = input("Enter element you want to store\nEnter int = Integer\tfloat = Floatin value\tstr = String")
    elif(a == int or INT or Int):
        x = int(input("Enter a interger value: "))
        l.append(x)
    else:
        print("Enter a valid data type")
    r += 1
print(l,type(l))
