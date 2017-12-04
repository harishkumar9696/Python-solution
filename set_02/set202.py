'''
Name:set202.py 
Description: ispower() 
Author:<harish>
Version:0.1
date:4/12/17

'''




def is_power(a,b):
    if a == b:
        return True
    if a % b == 0 and a/b%b==0:
        return True
    return False

a=raw_input("Enter a ")
b=raw_input("Enter b")
n1=int(a)
n2=int(b)
c=is_power(n1,n2)
print c