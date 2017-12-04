'''
Name:set108.py 
Description: Vector division
Author:<harish>
Version:0.1
date:4/12/17

'''

def getRatios(vect1, vect2):
    ratios=[]
    for i in range(len(vect1)):
        vect1e=float(vect1[i])
        vect2e=float(vect2[i])
        ratios.append(vect1e/vect2e)
    return ratios
vect1=[5,9,2,6]
vect2=[8,9,2,6]

c=getRatios(vect1,vect2)
print c