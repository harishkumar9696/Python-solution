
'''
Name:set307.py 
Description: use_only
Author:<harish>
Version:0.1
date:06/12/2017
'''
def using_only(str1,str2):
    i=0
    while i<len(str1):
        if str1[i] in str2:
            i=i+1
        else:
            return False
    return True

str1=raw_input("enter the string")
str2=raw_input("enter the use_only letters")
c= using_only(str1,str2)
print c
