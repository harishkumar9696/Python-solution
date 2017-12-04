'''
Name:set106.py 
Description: decimal add
Author:<harish>
Version:0.1
date:4/12/17

'''

s=raw_input("enter numbers: ")
s.split(',')
sum=0
for i in s.split(','):
    sum=sum+float(i)
    print "sum of the numbers is "+str(sum)
