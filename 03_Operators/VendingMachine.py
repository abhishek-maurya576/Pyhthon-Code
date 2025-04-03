#Write a program to simulate a vending machine where you input money and select items. Use comparison and logical operators to calculate the remaining balance or error.
print("1. Sugar(40/kg)\t2. Almend(500/kg)\n3. Chips(20/peace)\t4. Exit")
mny = int(input("Enter Money here: "))
print("You entered money is: ",mny)
while True :
    print("===================================\n1. Sugar(40/kg)\t2. Almend(500/kg)\n3. Chips(20/peace)\t4. Exit\n=======================================================")
    
    op = int(input("Choose an Item: "))
    
    if(op == 1):
        amt = int(input("Enter your amount(kg): "))
        sugaramt = amt*40
        print("Total amount of sugar: ",sugaramt)
        op1 = int(input("Enter 1 for confirmation or 0 for denial: "))
        if(op1 == 1 and mny >= sugaramt):
            print("Take your sugar\nHave a nice day!")
            mny -= sugaramt
            print("You have",mny,"ruppey to left")
        elif(op1 == 1 and mny < sugaramt):
                print("You have not enough money to buy")
                break
        elif (op1 == 0):
            print("Cancelation successfully")
        else:
            print("Something went wrong!")
    elif(op == 2):
        amt = int(input("Enter your amount(kg): "))
        almndamt = amt*500
        print("Total amount of Almond is: ",almndamt)
        op1 = int(input("Enter 1 for confirmation or 0 for denial: "))
        if(op1 == 1 and mny >= almndamt):
            print("Take your almond\nHave a nice day!")
            mny -= almndamt
            print("You have",mny,"ruppey to left")
        elif(op1 == 1 and mny < almndamt):
                print("You have not enough money to buy")
                break
        elif (op1 == 0):
            print("Cancelation successfully")
        else:
            print("Something went wrong!")

    elif(op == 3):
        amt = int(input("Enter your peace: "))
        chipsamt = amt*20
        print("Total amount of Chips is: ",chipsamt)
        op1 = int(input("Enter 1 for confirmation or 0 for denial: "))
        if(op1 == 1 and mny >= chipsamt):
            print("Take your chips\nHave a nice day!")
            mny -= chipsamt
            print("You have",mny,"ruppey to left")
        elif(op1 == 1 and mny < chipsamt):
                print("You have not enough money to buy")
                break
        elif (op1 == 0):
            print("Cancelation successfully")
        else:
            print("Something went wrong!")
    elif (op == 4):
        print("Thans for using")
        break
    else:
        print("Choose valid option\nSomething went wrong\n====================")
   
if (mny != 0):
    print("Take your cash: ",mny)
