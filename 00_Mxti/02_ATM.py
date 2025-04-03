
initial_bal = 0.00
while True:
    print("Welcome to the XYZ ATM\n1. Check Balance\t2. Withdraw\n3. Deposite\t4. Exit\n==========")
    op = int(input("Choose an options: "))
    if op == 1:
        print("You have: ",initial_bal,"INR")
    elif op == 2:
        withdraw = float(input("Enter an amount to be withdraw: "))
        if 0<= withdraw >= initial_bal:
            if initial_bal-withdraw >= 0:
                initial_bal-=withdraw
                print("Take your cash :)\nRemaining balance: ",initial_bal)
            else:
                print("Please enter positive number")
        elif withdraw < 0:
            print("Please enter positive number")
        else:
            print("You have not Enough balance")
    elif op == 3:
        deposite = float(input("Enter an amount to be deposite: "))
        initial_bal+=deposite
        print("You have successfully deposite: ",deposite,"INR\nTotal balance is: ",initial_bal)
    elif op == 4:
         print("Thanks For Using 'Have a nice day'")
         break
    else:
        print("Choose an valid options")
