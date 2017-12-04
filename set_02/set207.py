'''
Name:set207.py 
Description: palindrome
Author:<harish>
Version:0.1
date:4/12/17

'''
def is_palindrome(my_str):
    letters = []
    for c in my_str:
        if c.isalpha():
            letters.append(c)
    return letters == letters[::-1]
str=raw_input("Enter a string")
c=is_palindrome(str)
print c