
'''
Name:set203.py 
Description: factorial() 
Author:<harish>
Version:0.1
date:4/12/17

'''

def factorial(n):
    num=1
    while n >= 1:
        num = num * n
        n = n - 1
    return num
num1=raw_input("Enter the number")
num2=int(num1)
c=factorial(num2)
print c
