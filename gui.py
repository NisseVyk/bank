import customtkinter
#from PIL import Image


class App(customtkinter.CTk):
    accounts = ""
    logged_in_as = ""
    def __init__(self, accounts):
        super().__init__()
        self.accounts = accounts

        self.title("Banken")
        self.geometry("250x170")

        self.account_number_entry = customtkinter.CTkEntry(self, width=160, height=40, placeholder_text="Account Number:")
        self.account_number_entry.grid(row=0, column=1, padx=45, pady=10)

        self.password_entry = customtkinter.CTkEntry(self, width=160, height=40, placeholder_text="Password:")
        self.password_entry.grid(row=1, column=1, padx=45)

        self.button = customtkinter.CTkButton(self, width=100, height=25, text="Login", command=self.login)
        self.button.grid(row=2, column=1, padx=45, pady=15)
        print(self.accounts)

    def login(self):
        account_number = self.account_number_entry.get()
        password = self.password_entry.get()

        for account in self.accounts:
            if account.number == account_number:
                print("yes")

def schizo():
    print("SHADOW WIZARD MONEY GANG")