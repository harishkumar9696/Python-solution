'''
Name:set206.py 
Description: 1st even no
Author:<harish>
Version:0.1
date:4/12/17

'''
def findAnEven(l): 
    for i in l: 
        if int(i) % 2 == 0: 
            return i 
    raise ValueError("No even numbers in list!") 

a=raw_input("enter numbers")
l=[]
for i in a:
    l.append(i)
out=findAnEven(l)
print out