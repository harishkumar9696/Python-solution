'''
Name:set208.py 
Description: evaluate
Author:<harish>
Version:0.1
date:4/12/17

'''

def eval_loop():
    while True:
        a = raw_input('enter the expression to be evaluated: ')
        if a == 'done':
            break
        else:
            result = eval(a)
            print result
    
eval_loop()