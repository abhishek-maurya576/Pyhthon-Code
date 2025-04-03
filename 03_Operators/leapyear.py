#Write a program to check if a given year is a leap year using logical operators.
year = int(input("Enter year (YYYY): "))
if(year % 4 == 0 or year % 400 == 0):
    print("Leap year")
elif (year % 100 ):
    print("Is not leap year")
else:
    print("Not a leap year")
