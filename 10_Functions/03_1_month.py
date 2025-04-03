#write a function that take an integer from 1 to 12,represent the monts and display the corresponding month(i.e. 1 = JANUARY)
def get_months(month):
    months = {
        1:'January',2:'February',3:'March',4:'April',
        5:'May',6:'JUne',7:'July',8:'August',9:'September',10:'October',
        11:'November',12:'December',
    }
    if 1 <= month <=12:
        return months[month]
    else:
        return "Enter a number between 1 to 12"
num = int(input("Enter a number in between 1 to 12: "))
print(get_months(num))
