'''
Name:set301.py 
Description: palindrome
Author:<harish>
Version:0.1
date:06/12/2017
'''

def is_palindrome(str):
    str2=str[::-1]
    if str==str2:
        print("It is a Palindrome") 
    else:
        print("Not a Palindrome")
str=raw_input("Enter a string:")
is_palindrome(str)
