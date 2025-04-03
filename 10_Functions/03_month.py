#write a function that take an integer from 1 to 12,represent the monts and display the corresponding month(i.e. 1 = JANUARY)
num = int(input("Enter a number in between 1 to 12: "))
def month(month):
    if month == 1:
        return 'JANUARY'
    elif month == 2:
        return 'FEBRUARY'
    elif month == 3:
        return 'MARCH'
    elif month == 4:
        return 'APRIL'
    elif month == 5:
        return 'MAY'
    elif month == 6:
        return 'JUNE'
    elif month == 7:
        return 'JULY'
    elif month == 8:
        return 'AUGUST'
    elif month == 9:
        return 'SEPTEMBER'
    elif month == 10:
        return 'OCTOBER'
    elif month == 11:
        return 'NOVEMBER'
    elif month == 12:
        return 'DECEMBER'
    else:
        return "Enter a number between 1 to 12"
print(month(num))
