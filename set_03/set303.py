'''
Name:set303.py 
Description: has_noe()
Author:<harish>
Version:0.1
date:06/12/2017
'''

def has_noe(str):
    if 'e' in str:
        print("it has e")
    elif 'E' in str:
        print("It has e")
    else:
        print("It has no e")
          
          
str=raw_input("enter string")
has_noe(str)