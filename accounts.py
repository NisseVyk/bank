import pickle
import random
import os

account_list = []

class Accounts:
    def __init__(self, number : str, pincode : str, fname : str, lname : str, balance : int):
        self.number = number
        self.pincode = pincode
        self.fname = fname
        self.lname = lname
        self.balance = balance

def clear():    
    os.system("cls" if os.name == 'nt' else 'clear')


def save_file(accounts):
    with open('account.bin', 'wb') as account_list_file:
        pickle.dump(accounts, account_list_file)

def clear_file():
    account_list = []
    with open('account.bin', 'wb') as account_list_file:
        pickle.dump(account_list, account_list_file)

def login(account_number, pincode):
    for account in account_list:
        print(account)
        if account_number == account.number:
            input(1)
            if pincode == account.pincode:
                return account
            else:
                return "404"
        else:
            return "404"
             
def create_account(fname, lname, pin):
        while True:
            number = random.randint(100000000, 999999999)
            unique = True
            i= 0
            while i < len(account_list):
                if number == account_list[i].number:
                    unique = False
                i+=1
            if unique:
                break

        account_list.append(Accounts(str(number), str(pin), fname, lname, 0))
        print(account_list)
        save_file(account_list)


def get_account_list():
    with open('account.bin', 'rb') as account_list_file:
        account_list = pickle.load(account_list_file)
    
    return account_list

with open('account.bin', 'rb') as account_list_file:
    account_list = pickle.load(account_list_file)