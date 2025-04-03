#Check whether a number is a palindrome (e.g., 121 is a palindrome).
num = input("Enter a number: ")
n = int(num)
palindrom = 0
if n%2 == 0:
    print("the number %d is not palindrome"%n)
else:
    i,j = 0,1
    while i<n:
        if num[i] == num[i-j]:
            palindrom = 1
        i += 1
        j += 2
    print("The number %d is palindrome number"%int(num))
