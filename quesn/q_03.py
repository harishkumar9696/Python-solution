'''
Name: q_03.py 
Description: GCD for a list of numbers
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
print reduce(gcd,[25,35,45,49])
