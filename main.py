import accounts
import gui
import time

import os
def clear():    
    os.system("cls" if os.name == 'nt' else 'clear')

app = gui.App(accounts.account_list)

app.mainloop()
