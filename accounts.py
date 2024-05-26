import pickle
import random
import os
try:
    from pymongo import MongoClient
except:
    input('Run: python -m pip install "pymongo[srv]"')
    exit()

account_list = []

class Accounts:
    def __init__(self, number : str, pincode : str, fname : str, lname : str, balance : int):
        self.number = number
        self.pincode = pincode
        self.fname = fname
        self.lname = lname
        self.balance = balance

def login(account_number, pincode):
    print(account_list)
    i=0
    while i<len(account_list):
        if account_number == account_list[i]["number"]:
            if pincode == account_list[i]["pincode"]:
                return account_list[i]
            else:
                return "404"
        elif i == len(account_list)-1:
            return "404"
        i+=1

             
def create_account(fname, lname, pin):
        while True:
            number = random.randint(100000000, 999999999)
            unique = True
            i= 0
            while i < len(account_list):
                if number == account_list[i]["number"]:
                    unique = False
                i+=1
            if unique:
                break
        
        account = {"number" : str(number), "pincode" : str(pin), "fname" : fname, "lname" : lname, "balance" : 0}
        db = get_collection()
        db.insert_one(account)
        
def update_balance(number, new_balance):
    account = { "number": number }
    newvalues = { "$set": { "balance": new_balance } }

    db = get_collection()
    db.update_one(account, newvalues)

def transfer_money(from_number, to_number, amount):
    get_account_list()

    for account in account_list:
        if account["number"] == from_number:
            from_balance = account["balance"] - amount
            break

    for account in account_list:
        if account["number"] == to_number:
            to_balance = account["balance"] + amount

    update_balance(from_number, from_balance)
    update_balance(to_number, to_balance)

    get_account_list()

def get_collection():
    connection_string = "mongodb+srv://dbuser:ballefjong@bankdb.caczuaa.mongodb.net/?retryWrites=true&w=majority&appName=bankdb"

    client = MongoClient(connection_string)

    return client['bank_data']["data"]

def get_account_list():
    db = get_collection()
    item_details = db.find()
    for item in item_details:
        account_list.append(item)

get_account_list()
print(account_list)
