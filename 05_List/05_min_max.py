#Write a program that takes a list of numbers and prints the maximum and minimum values.
n = int(input("Enter a list capacity: "))
lst =[]
i=0
while i<n:
	print("Enter list item %d: "%(i+1),end=" ")
	lst_value = int(input())
	lst.append(lst_value)
	i += 1
print("the max value is ",max(lst))
print("the max value is ",min(lst))
