'''
Name: q_01.py 
Description: Palindrome without using string functions
Author:<harish>
Version:0.1
date:08/12/2017
'''


def is_palindrome(st):
    length=len(st)
    i=0
    while length>0:
        if st[i]==st[length-1]:
            i+=1
            length-=1
        else:
            return False 
            
    return True    
            
st=raw_input("Enter a string to check whether it is palindrome or not:\n")
print is_palindrome(st)
 