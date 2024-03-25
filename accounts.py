import pickle
import random
import os
import time


class Accounts:
    def __init__(self, number, pincode, fname, lname, balance):
        self.number = number
        self.pincode = pincode
        self.fname = fname
        self.lname = lname
        self.balance = balance


def clear():    
    os.system("cls" if os.name == 'nt' else 'clear')

account_list = []
def read_file():
    with open('account.dict', 'rb') as account_list_file:
        global account_list
        account_list = pickle.load(account_list_file)

def save_file():
    with open('account.dict', 'wb') as account_list_file:
        pickle.dump(account_list, account_list_file)

def clear_file():
    account_list = []
    with open('account.dict', 'wb') as account_list_file:
        pickle.dump(account_list, account_list_file)

def login(account_number, pincode):
    for account in account_list:
         if account.number == account_number:
             if account.pincode == pincode:
                 clear()
                 print(f"Login correct, welcome {account.fname} {account.lname}")
                 time.sleep(3)
                 return account
    

def create_account():
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
    
    clear()
    fname = input("What's your first name?\n")
    clear()
    lname = input("What's your last name?\n")
    clear()
    pincode = input("What do you want your pin code to be?")
    account_list.append(Accounts(str(number), str(pincode), fname, lname, 0))
    save_file()
    input(number)