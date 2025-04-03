a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
c = int(input("Enter the value of c: "))
print(a,'x^2 +',b,'x +',c,sep = "")

print("\n%dx^2 + "%a,end="")
print("%dx + "%b,end="")
print("%d\n"%c)
print("%dx^2 + %dx + %d"%(a,b,c))
