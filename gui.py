import customtkinter
import accounts



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
    
    def create_login(self):
        self.account_number_entry = customtkinter.CTkEntry(self, width=160, height=40, placeholder_text="Account Number:")
        self.account_number_entry.grid(row=0, column=1, padx=45, pady=10)

        self.password_entry = customtkinter.CTkEntry(self, width=160, height=40, placeholder_text="Pin:")
        self.password_entry.grid(row=1, column=1, padx=45)

        self.login_button = customtkinter.CTkButton(self, width=100, height=25, text="Login", command=self.login)
        self.login_button.grid(row=2, column=1, padx=45, pady=15)

        self.create_account_button = customtkinter.CTkButton(self, width=80, height=15, fg_color="transparent", text="Create Account", command=self.create_account_creator)
        self.create_account_button.grid(row=3, column=1, padx=55)

    def create_home(self):
        self.grid_rowconfigure(5, weight=1)
        self.grid_columnconfigure(2, weight=1)
        
        accounts.get_account_list()

        self.name = customtkinter.CTkLabel(self, width=200, height=40, text=f'{self.logged_in_as["fname"]} {self.logged_in_as["lname"]}')
        self.name.grid(row=0, column=1, padx=45, pady=10)
        self.balance = customtkinter.CTkLabel(self, width=160, height=40, text="Balance: $" + str(self.logged_in_as["balance"]))
        self.balance.grid(row=0, column=3, padx=45, pady=10)

        self.deposit = customtkinter.CTkButton(self, width=180, height=40, text="Deposit", command=self.create_deposit)
        self.deposit.grid(row=3, column=2, pady=10)
        self.undeposit = customtkinter.CTkButton(self, width=180, height=40, text="Withdraw", command=self.create_withdraw)
        self.undeposit.grid(row=4, column=2, pady=10)
        self.transfer = customtkinter.CTkButton(self, width=180, height=40, text="Transfer", command=self.create_transfer)
        self.transfer.grid(row=5, column=2, pady=10)

        self.log_out_button = customtkinter.CTkButton(self, width=100, height=40, text="Log out", command=self.log_out)
        self.log_out_button.grid(row=7, column=1, pady=20)

    def create_account_creator(self):
        self.destroy()

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

        self.destroy()

        self.grid_rowconfigure(6, weight=1)
        self.grid_columnconfigure(2, weight=1)

        self.name = customtkinter.CTkLabel(self, width=200, height=40, text=f'{self.logged_in_as["fname"]} {self.logged_in_as["lname"]}')
        self.name.grid(row=0, column=1, padx=45, pady=10)
        self.balance = customtkinter.CTkLabel(self, width=160, height=40, text="Balance: $" + str(self.logged_in_as["balance"]))
        self.balance.grid(row=0, column=3, padx=45, pady=10)

        self.how_much = customtkinter.CTkLabel(self, width=180, height=40, text="How much do you want to deposit?")
        self.how_much.grid(row=2, column=2, pady=10)
        self.amount = customtkinter.CTkEntry(self, width=160, height=40, placeholder_text="Amount:")
        self.amount.grid(row=3, column=2, pady=10)
        self.action = customtkinter.CTkButton(self, width=160, height=40, text="Deposit", command=self.deposit_money)
        self.action.grid(row=4, column=2, pady=10)
        self.back = customtkinter.CTkButton(self, width=160, height=40, text="Back", command=self.cancel)
        self.back.grid(row=5, column=2, pady=10)

    def create_withdraw(self):
        self.destroy()

        self.grid_rowconfigure(6, weight=1)
        self.grid_columnconfigure(2, weight=1)

        self.name = customtkinter.CTkLabel(self, width=200, height=40, text=f'{self.logged_in_as["fname"]} {self.logged_in_as["lname"]}')
        self.name.grid(row=0, column=1, padx=45, pady=10)
        self.balance = customtkinter.CTkLabel(self, width=160, height=40, text="Balance: $" + str(self.logged_in_as["balance"]))
        self.balance.grid(row=0, column=3, padx=45, pady=10)

        self.how_much = customtkinter.CTkLabel(self, width=180, height=40, text="How much do you want to withdraw?")
        self.how_much.grid(row=2, column=2, pady=10)
        self.amount = customtkinter.CTkEntry(self, width=160, height=40, placeholder_text="Amount:")
        self.amount.grid(row=3, column=2, pady=10)
        self.action = customtkinter.CTkButton(self, width=160, height=40, text="Withdraw", command=self.withdraw_money)
        self.action.grid(row=4, column=2, pady=10)
        self.back = customtkinter.CTkButton(self, width=160, height=40, text="Back", command=self.cancel)
        self.back.grid(row=5, column=2, pady=10)

    def create_transfer(self):
        self.destroy()

        self.grid_rowconfigure(6, weight=1)
        self.grid_columnconfigure(2, weight=1)

        self.name = customtkinter.CTkLabel(self, width=200, height=40, text=f'{self.logged_in_as["fname"]} {self.logged_in_as["lname"]}')
        self.name.grid(row=0, column=1, padx=45, pady=10)
        self.balance = customtkinter.CTkLabel(self, width=160, height=40, text="Balance: $" + str(self.logged_in_as["balance"]))
        self.balance.grid(row=0, column=3, padx=45, pady=10)

        self.text = customtkinter.CTkLabel(self, width=200, height=40, text="Transfer money")
        self.text.grid(row=2, column=2, pady=10)
        self.account_number_label = customtkinter.CTkLabel(self, width=170, height=40, text=f'From: {self.logged_in_as["number"]}')
        self.account_number_label.grid(row=3, column=2, pady=10)
        self.amount = customtkinter.CTkEntry(self, width=200, height=40, placeholder_text="Amount:")
        self.amount.grid(row=4, column=2, pady=10)
        self.account_number_entry = customtkinter.CTkEntry(self, width=200, height=40, placeholder_text="To:",)
        self.account_number_entry.grid(row=5, column=2, pady=10)
        
        self.transfer_button = customtkinter.CTkButton(self, width=200, height=40, text="Transfer", command=self.transfer_money)
        self.transfer_button.grid(row=6, column=2, pady=10)
        self.back = customtkinter.CTkButton(self, width=160, height=40, text="Back", command=self.cancel)
        self.back.grid(row=7, column=2)


    def destroy(wid):
        for item in wid.winfo_children():
            item.destroy()

    def login(self):
        account_number = self.account_number_entry.get()
        pin = self.password_entry.get()
        login = accounts.login(account_number, pin)
        print(login)
        if type(login) == str:
            self.account_number_entry.destroy()
            self.account_number_entry = customtkinter.CTkEntry(self, width=160, height=40, placeholder_text="Account Number:", border_color="red", )
            self.account_number_entry.grid(row=0, column=1, padx=45, pady=10)
            self.password_entry.destroy()
            self.password_entry = customtkinter.CTkEntry(self, width=160, height=40, placeholder_text="Pin", border_color="red")
            self.password_entry.grid(row=1, column=1, padx=45)

        else:
            self.logged_in_as = login
            self.destroy()
            self.create_home()
  
    def log_out(self):
        self.logged_in_as = ""
        self.destroy()
        accounts.get_account_list()
        self.create_login()

    def create_account(self):
        fname = self.fname_input.get()
        lname = self.lname_input.get()
        pin = self.pin_input.get()
        accounts.create_account(fname, lname, pin)
        self.destroy()
        self.create_login()
        self.account_list = accounts.get_account_list()

    def deposit_money(self):
        amount = self.amount.get()
        try:
            self.logged_in_as["balance"] += int(amount)
            accounts.update_balance(self.logged_in_as["number"], self.logged_in_as["balance"])
            self.destroy()
            self.create_home()
        except:
            self.amount.destroy()
            self.amount = customtkinter.CTkEntry(self, width=160, height=40, placeholder_text="Invalid input", placeholder_text_color="red", border_color="red")
            self.amount.grid(row=3, column=2, pady=10)
    
    def withdraw_money(self):
        amount = self.amount.get()
        try:
            if self.logged_in_as["balance"] > int(amount):
                self.logged_in_as["balance"] -= int(amount)
                accounts.update_balance(self.logged_in_as["number"], self.logged_in_as["balance"])
                self.destroy()
                self.create_home()
            else:
                self.amount.destroy()
                self.amount = customtkinter.CTkEntry(self, width=160, height=40, placeholder_text="Not enough money", placeholder_text_color="red", border_color="red")
                self.amount.grid(row=3, column=2, pady=10)

        except:
            self.amount.destroy()
            self.amount = customtkinter.CTkEntry(self, width=160, height=40, placeholder_text="Invalid input", placeholder_text_color="red", border_color="red")
            self.amount.grid(row=3, column=2, pady=10)

    def transfer_money(self):
        from_number = self.logged_in_as["number"]
        to_number = self.account_number_entry.get()
        try:
            amount = int(self.amount.get())
        except:
            self.amount.destroy()
            self.amount = customtkinter.CTkEntry(self, width=200, height=40, placeholder_text="Invalid input", placeholder_text_color="red", border_color="red")
            self.amount.grid(row=4, column=2, pady=10)


        if self.logged_in_as["balance"] < amount:
            self.amount.destroy()
            self.amount = customtkinter.CTkEntry(self, width=200, height=40, placeholder_text="Not enough money", placeholder_text_color="red", border_color="red")
            self.amount.grid(row=4, column=2, pady=10)
        else:
            exist = False
            for account in self.account_list:
                if account["number"] == to_number:
                    exist = True
                    break

            if exist and from_number != to_number:
                self.destroy()

                self.sure = customtkinter.CTkLabel(self, width=300, height=40, text=f'Do you want to transfer ${amount} to {to_number}?')
                self.sure.grid(row=0, column=2, pady=20)

                self.yes = customtkinter.CTkButton(self, width=200, height=40, text="Yes", command= lambda : self.commit_transfer(to_number, amount))
                self.yes.grid(row=1, column=2, pady=10)
                self.no = customtkinter.CTkButton(self, width=200, height=40, text="Home", command=self.cancel)
                self.no.grid(row=2, column=2, pady=10)
            else:
                self.account_number_entry.destroy()
                self.account_number_entry = customtkinter.CTkEntry(self, width=200, height=40, placeholder_text="Invalid number", placeholder_text_color="red", border_color="red")
                self.account_number_entry.grid(row=5, column=2, pady=10)

    def cancel(self):
        self.destroy()
        self.create_home()

    def commit_transfer(self, to_number, amount):
        accounts.transfer_money(self.logged_in_as["number"], to_number, amount)

        self.account_list = accounts.account_list

        for account in self.account_list:
            if self.logged_in_as["number"] == account["number"]:
                self.logged_in_as = account

        self.destroy()
        self.create_home()