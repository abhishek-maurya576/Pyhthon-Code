l = []
n = int(input("Enter the line number: "))
i = 1
while i<=n:
	xx = input("Enter your Cities name: ")
	l.append(xx)
	i += 1
x = open('xyz.txt','w')
y = x.writelines(l)