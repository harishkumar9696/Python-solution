'''
Name: q_04.py 
Description: LCM of list of numbers 
Author:<harish>
Version:0.1
date:08/12/2017
'''

def lcm(x, y):
    if x>y:
      greater = x
    else:
      greater = y
    while(True):
      if((greater%x== 0) and (greater% y==0)):
        lcm = greater
        break
      greater += 1
    return lcm
  
num1=[1,2,3,4]
result=reduce(lcm,num1)
print(result)
