from customtkinter import *

def schizo():
    print("SHADOW WIZARD MONEY GANG")
bank = CTk()

bank.title("Banken")
bank.geometry("500x500")
button = CTkButton(bank, text="knap", command=schizo)
button.grid(row=0, column=0, padx=20, pady=20)

bank.mainloop()