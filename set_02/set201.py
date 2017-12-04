'''
Name:set201.py 
Description: gcd 
Author:<harish>
Version:0.1
date:4/12/17

'''



def gcd(a, b):
    if a > b:
        r = a % b
        if r == 0:
            print b
        else:
            return gcd(b, r)
    if a < b:
        r = b % a
        if r == 0:
            print a
        else:
            return gcd(a, r)
number1=raw_input("enter first number")
number2=raw_input("enter second number")
number1=int(number1)
number2=int(number2)
gcd(number1,number2)