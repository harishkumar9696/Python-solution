'''
Name:set107.py 
Description: IsIn function
Author:<harish>
Version:0.1
date:4/12/17

'''

def IsIn(a,b):
    b in a 
    if True:
        print("Entered check string is found inside the string")
    else: 
        print("Entered check string is not found inside the string")
  
a=raw_input("Enter a string:")
b=raw_input("Enter a check string:")
IsIn(a,b)