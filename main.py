import accounts
import time
import os
def clear():    
    os.system("cls" if os.name == 'nt' else 'clear')

accounts.read_file()


while True:
    while True:
        clear()
        user_input = input("What do you want to do?\n\t1. Login\n\t2. Create account\n\t3. Remove account\n\t4. Delete\n")

        match user_input:
            case "1":
                clear()
                global account
                account_number = input("What's your account number?\n")
                clear()
                pincode = input("What's your pincode?\n")
                account = accounts.login(account_number, pincode)
                if type(account) == accounts.Accounts:
                    break
                else:
                    print("Wrong pin or account number")
                    time.sleep(3)
            case "2":
                accounts.create_account()
            case "4":
                accounts.clear_file()
    
    while True:
        clear()
        user_input = input("What do you want to do today?\n\n\t1. Deposit money\n\t2. Withdraw money\n\t3. Tranfer money\n\t")
