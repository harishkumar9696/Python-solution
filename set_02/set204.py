'''
Name:set204.py 
Description: number equivalent of binary 
Author:<harish>
Version:0.1
date:4/12/17

'''
binary = raw_input('enter a number: ')
decimal = 0
for digit in binary:
    decimal = decimal*2 + int(digit)
print decimal