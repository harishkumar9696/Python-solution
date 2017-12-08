'''
Name: q_02.py 
Description: GCD
Author:<harish>
Version:0.1
date:08/12/2017
'''

def gcd(no1,no2):
    if(no2==0):
        return no1
    elif((no1%no2)==0):
        return no2
    else:
        a=no1%no2
        return gcd(no2,a)
no1=int(raw_input("enter a number"))
no2=int(raw_input("enter another number"))
print gcd(no1,no2)