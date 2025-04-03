#Check whether a number is Armstrong or not (e.g., 153 = 1³ + 5³ + 3³).
num = input('Enter a number: ')
p = len(num)
n = int(num)
arm = 0
for x in num:
    arm += int(x)**p
if arm == n:
    print('The number %d is armstrong number'%int(num))
else:
    print('The number %d is not armstrong number'%int(num))
    
