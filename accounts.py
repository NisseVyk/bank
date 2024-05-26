import pickle
import random
import os
from pymongo import MongoClient

account_list = []

class Accounts:
    def __init__(self, number : str, pincode : str, fname : str, lname : str, balance : int):
        self.number = number
        self.pincode = pincode
        self.fname = fname
        self.lname = lname
        self.balance = balance

def login(account_number, pincode):
    for account in account_list:
        print(account)
        if account_number == account["number"]:
            if pincode == account["pincode"]:
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
