#!/usr/bin/env python
# coding: utf-8

# In[5]:


import os
from pathlib import Path
from Section2Question1 import Account

class DevAccount:
    def __init__(self,name):
        Account.__init__(self,name)

    def GetBalance(self, name):
        name=input('Enter Account Number to Get Balance:'+"\n")
        Account.__init__(self,name)
        print("Current Balance for Account", name, "is","MYR", self.balance)
        Account.commit(self) 
        
    def SetBalance(self, name):
        Account.__init__(self,name)
        Account.commit(self)
        newBalance=input('Enter New Account Balance:'+"\n")
        self.balance = newBalance
        print("New Balance for Account", name, "is","MYR", self.balance)
        Account.commit(self)
            
    def Transfer(self,sender,recepient,amount):
        print("Old Balance for Account", sender, "is","MYR", self.balance)
        Account.__init__(self,sender)
        Account.withdraw(self,amount,sender)
        Account.commit(self)
        name=recepient
        print("Old Balance for Account", recepient, "is","MYR", self.balance)
        Account.__init__(self,recepient)
        Account.deposit(self,amount,recepient)
        Account.commit(self)
        
    def commit(self):
        with open(self.filepath+".txt",'a') as file:
            file.seek(0, os.SEEK_END)
            file.write(str(self.balance)+"\n")
    def __str__(self):
        return f"{self.name}'s account. Balance: {self.balance}"
    
name= input('Enter Account Number for quick Balance:'+"\n")
account=DevAccount(name)

status = True
while status == True :
    option=input('Choose Option 1 to Get Balance, Option 2 to Manually Set Balance, Option 3 to do a Transfer and Option 4 to Exit'+"\n")
    if option == "1":
        account.GetBalance(name)
        status == True
    elif option == "2":
        account.SetBalance(input("Enter Account number to change Balance:"+"\n"))
        status == True
    elif option == "3":
        account.Transfer(input("enter Sender Account Number:"+"\n"),input("enter Recipient Account Number:"+"\n"),int(input("enter Amount to transfer:"+"\n")))
        status == True
    elif option == "4":
        print("Thank you. Goodbye"+"\n")
        status = False
    else:
         print("Option does not exist. Please Try again"+"\n")      


# ## 

# In[ ]:




