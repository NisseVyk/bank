import customtkinter
import accounts
import random


class App(customtkinter.CTk):
    account_list = ""
    logged_in_as = ""
    def __init__(self, accounts):
        super().__init__()
        self.account_list = accounts
        self.logged_in_as = ""
        self.title("Banken")
        self.geometry("900x600")

        self.create_login()
        #self.destroy_login()
        #self.create_home()
    
    def create_login(self):
        self.account_number_entry = customtkinter.CTkEntry(self, width=160, height=40, placeholder_text="Account Number:")
        self.account_number_entry.grid(row=0, column=1, padx=45, pady=10)

        self.password_entry = customtkinter.CTkEntry(self, width=160, height=40, placeholder_text="Password:")
        self.password_entry.grid(row=1, column=1, padx=45)

        self.login_button = customtkinter.CTkButton(self, width=100, height=25, text="Login", command=self.login)
        self.login_button.grid(row=2, column=1, padx=45, pady=15)

        self.create_account_button = customtkinter.CTkButton(self, width=80, height=15, fg_color="transparent", text="Create Account", command=self.create_account_creator)
        self.create_account_button.grid(row=3, column=1, padx=55)

    def destroy_login(self):
        self.account_number_entry.destroy()
        self.password_entry.destroy()
        self.login_button.destroy()
        self.create_account_button.destroy()


    def create_home(self):
        self.grid_rowconfigure(5, weight=1)
        self.grid_columnconfigure(2, weight=1)
        
        self.name = customtkinter.CTkLabel(self, width=200, height=40, text=f"{self.logged_in_as.fname} {self.logged_in_as.lname}")
        self.name.grid(row=0, column=1, padx=45, pady=10)
        self.balance = customtkinter.CTkLabel(self, width=160, height=40, text="Balance: $" + str(self.logged_in_as.balance))
        self.balance.grid(row=0, column=3, padx=45, pady=10)

        self.deposit = customtkinter.CTkButton(self, width=180, height=40, text="Deposit", command=self.create_deposit)
        self.deposit.grid(row=3, column=2, pady=10)
        self.undeposit = customtkinter.CTkButton(self, width=180, height=40, text="Withdraw", command=self.create_withdraw)
        self.undeposit.grid(row=4, column=2, pady=10)

    def destroy_home(self):
        self.name.destroy()
        self.balance.destroy()
        self.deposit.destroy()
        self.undeposit.destroy()

    def create_account_creator(self):
        self.destroy_login()

        self.grid_rowconfigure(5, weight=1)
        self.grid_columnconfigure(2, weight=1)

        self.title = customtkinter.CTkLabel(self, width=200, height=40, text="Create Account")
        self.title.grid(row=0, column=2, padx=45, pady=20)

        self.fname_input = customtkinter.CTkEntry(self, width=160, height=40, placeholder_text="First Name:")
        self.fname_input.grid(row=1, column=2, pady=5)
        self.lname_input = customtkinter.CTkEntry(self, width=160, height=40, placeholder_text="Last Name:")
        self.lname_input.grid(row=2, column=2, pady=5)
        self.pin_input = customtkinter.CTkEntry(self, width=160, height=40, placeholder_text="Pin Code:")
        self.pin_input.grid(row=3, column=2, pady=5)
        self.create_account_button = customtkinter.CTkButton(self, width=160, height=40, text="Create Account", command=self.create_account)
        self.create_account_button.grid(row=4, column=2, pady=5)

    def create_deposit(self):

        self.destroy_home()

        self.grid_rowconfigure(6, weight=1)
        self.grid_columnconfigure(2, weight=1)

        self.name = customtkinter.CTkLabel(self, width=200, height=40, text=f"{self.logged_in_as.fname} {self.logged_in_as.lname}")
        self.name.grid(row=0, column=1, padx=45, pady=10)
        self.balance = customtkinter.CTkLabel(self, width=160, height=40, text="Balance: $" + str(self.logged_in_as.balance))
        self.balance.grid(row=0, column=3, padx=45, pady=10)

        self.how_much = customtkinter.CTkLabel(self, width=180, height=40, text="How much do you want to deposit?")
        self.how_much.grid(row=2, column=2, pady=10)
        self.amount = customtkinter.CTkEntry(self, width=160, height=40, placeholder_text="Amount:")
        self.amount.grid(row=3, column=2, pady=10)
        self.action = customtkinter.CTkButton(self, width=160, height=40, text="Deposit", command=self.deposit_money)
        self.action.grid(row=4, column=2, pady=10)

    def destroy_deposit(self):
        self.name.destroy()
        self.balance.destroy()
        self.how_much.destroy()
        self.amount.destroy()
        self.action.destroy()

    def create_withdraw(self):
        self.destroy_home()

        self.grid_rowconfigure(6, weight=1)
        self.grid_columnconfigure(2, weight=1)

        self.name = customtkinter.CTkLabel(self, width=200, height=40, text=f"{self.logged_in_as.fname} {self.logged_in_as.lname}")
        self.name.grid(row=0, column=1, padx=45, pady=10)
        self.balance = customtkinter.CTkLabel(self, width=160, height=40, text="Balance: $" + str(self.logged_in_as.balance))
        self.balance.grid(row=0, column=3, padx=45, pady=10)

        self.how_much = customtkinter.CTkLabel(self, width=180, height=40, text="How much do you want to withdraw?")
        self.how_much.grid(row=2, column=2, pady=10)
        self.amount = customtkinter.CTkEntry(self, width=160, height=40, placeholder_text="Amount:")
        self.amount.grid(row=3, column=2, pady=10)
        self.action = customtkinter.CTkButton(self, width=160, height=40, text="Withdraw", command=self.withdraw_money)
        self.action.grid(row=4, column=2, pady=10)

    def login(self):
        account_number = self.account_number_entry.get()
        password = self.password_entry.get()

        for account in self.account_list:
            if account_number == account.number:
                if password == account.pincode:
                    self.logged_in_as = account
                    self.destroy_login()
                    self.create_home()
                else:
                    print("fel lösen")

    def create_account(self):
        fname = self.fname_input.get()
        lname = self.lname_input.get()
        pin = self.pin_input.get()



    def deposit_money(self):
        amount = self.amount.get()
        try:
            self.logged_in_as.balance += int(amount)
            accounts.save_file(self.account_list)
            self.destroy_deposit()
            self.create_home()
        except:
            self.amount.destroy()
            self.amount = customtkinter.CTkEntry(self, width=160, height=40, placeholder_text="Invalid input", placeholder_text_color="red", border_color="red")
            self.amount.grid(row=3, column=2, pady=10)
    
    def withdraw_money(self):
        amount = self.amount.get()

        try:
            self.logged_in_as.balance -= int(amount)
            accounts.save_file(self.account_list)
            self.destroy_deposit()
            self.create_home()
        except:
            self.amount.destroy()
            self.amount = customtkinter.CTkEntry(self, width=160, height=40, placeholder_text="Invalid input", placeholder_text_color="red", border_color="red")
            self.amount.grid(row=3, column=2, pady=10)