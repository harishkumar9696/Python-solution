
'''
Name:set309.py 
Description: sorted
Author:<harish>
Version:0.1
date:06/12/2017
'''

def is_sorted(str):

    str2=[]

    for i in str:

        str2.append(i)

    str2.sort()

    if str2==str:

        print("True")

    else:

        print("False")

       
 
str=list(raw_input("Enter the string:"))

is_sorted(str)