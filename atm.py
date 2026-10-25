correct_pin = 1234
balance = 10000
i = 3
while i>0 :
    pin = int(input("Enter Your ATM PIN: "))
    if pin == correct_pin:
        ts = []
        print("""----MENU----
        Balance = 1
        Withdraw = 2
        Deposite = 3
        Exit = 4""")

       
        while True:
            menu= int(input("Enter a num from 1 to 4 to select a Menu option: "))
            if menu == 1:
                print("Balance is: ",balance)
            elif menu == 2:
                a = int(input("Enter amount you want to Withdraw:"))
                if 0< a < balance:
                    balance = balance-a
                    ts.append(f"Withdraw {a}")
                    print(f"{a} amount is deduted from amount")
                    print("Now current balance is: ",balance)
                elif a > balance:
                    print("insufficiant Fund")
                else:
                    print("Invalid Input")
            elif menu == 3:
                b = int(input("Enter amount to deposit: "))
                if 0<b:
                    balance+=b
                    ts.append(f"Deposit {b}")
                    print(f"{b} amount is credit to your bank account")
                    print("Now current balance is: ",balance)
                else:
                    print("Invalid input")
            elif menu < 0 or menu >5 :
                print("Invalid input enter num between 1 to 4 ")
                continue
            else:
                print("Thank you")
                for item in ts:
                    print(item)
                i = 0
                break


            

    else:
        i-=1
        print("Incorrect pin")
        print(f"{i} attempt left")
        if i == 0:
            print("Card blocked")
            i = 0