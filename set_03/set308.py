'''
Name:set308.py 
Description: abcderian 
Author:<harish>
Version:0.1
date:06/12/2017
'''

def abcderian(str):

    str2=[]

    for i in str:

        str2.append(i)

    str2.sort()

    if str2==str:

        print("True")

    else:

        print("False")

       
 
str=list(raw_input("Enter the string:"))

abcderian(str)