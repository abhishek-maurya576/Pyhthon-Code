#Write a program that takes a float input from the user, converts it into an integer, and prints the result.
fnum = float(input("Enter a float number: "))
print("input object class: ",type(fnum))
inum = int(fnum)
print("After converting in Interger: ",inum,"\nAfter converting in integer, now obj class",type(inum))
