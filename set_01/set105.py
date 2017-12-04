

'''
Name:set105.py 
Description: root and power
Author:<harish>
Version:0.1
date:4/12/17

'''

num = int(raw_input('Enter a positive integer: '))
power = 2
root = 1
ans = ''
while power < 6:
    while root**power <= num:
        if root**power == num:       
            print 'the root is ',root,
            print 'the power is ', power
            ans = True
        root =root+ 1        
    power =power+ 1
    root = 1
if ans != True:
    print'No such pair of integers exist'