#!/usr/bin/env python
# coding: utf-8

# In[3]:


import os
from pathlib import Path

class Account:

    def __init__(self, filepath):
        if Path(filepath+".txt").is_file():
            with open(filepath+".txt",'r') as file:
                self.filepath=filepath #create an instance variable from parameter of init function
                self.balance = int(file.readlines()[-1])
        else:
            print ("New Account Created")
            with open(filepath+".txt",'x') as file:
                self.filepath=filepath #create an instance variable from parameter of init function
                file.write("0000"+"\n")
            with open(filepath+".txt",'r') as file:
                self.filepath=filepath #create an instance variable from parameter of init function
                self.balance = int(file.readlines()[-1])
    def mybalance (self, name):
        print("Current Balance for Account", name, "is","MYR", self.balance)
        self.commit()
    def withdraw (self, amount,filepath):
        self.balance=self.balance - amount
        print("New Balance for Account", filepath, "is","MYR", self.balance)
        self.commit()
    def deposit (self, amount,filepath):
        self.balance= self.balance + amount
        print("New Balance for Account", filepath, "is","MYR", self.balance)
        self.commit()
    def commit(self):
        with open(self.filepath+".txt",'a') as file:
            file.seek(0, os.SEEK_END)
            file.write(str(self.balance)+"\n")
    def __str__(self):
        return f"{self.name}'s account. Balance: {self.balance}"

name=input('Enter Account Number:'+"\n")
account=Account(name)
status = True
while status == True :
    option=input('Choose Option 1 for Balance Enquiry, 2 to make a Deposit, 3 for Withdrawl and 4 to Exit'+"\n")
    if option == "2":
        account.deposit(int(input('Enter Amount to Deposit:'+"\n")),name)
        status == True
    elif option == "3":
        account.withdraw(int(input('Enter Amount to Withdraw:'+"\n")),name)
        status == True
    elif option == "1":
        account.mybalance(name)
        status == True        
    elif option == "4":
        print("Account Balance for", name, "is","MYR", account.balance)
        print("Thank you. Goodbye"+"\n")
        status = False
    else:
         print("Option does not exist. Please Try again"+"\n")      


# In[ ]:




