#!/usr/bin/env python
# coding: utf-8
#take user input
num = int(input("Enter a number: "))

#initialise value for factorial
factorial = 1

#calculate factorial number
if num < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   for i in range(1,num + 1):
       factorial = factorial*i
   print("\n""The factorial ! of ",num," is ",factorial,".\n",sep="")

#calculate total of digits in factorial
#turn number into string to iterate through and to do addition
sum = 0
for a in str(factorial):
  sum += int(a)
print("Sum of the digits in the value in ",num,"! is ", sum, sep="")



# In[ ]:




