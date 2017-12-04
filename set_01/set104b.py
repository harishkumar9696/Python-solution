'''
Name:set104b.py 
Description: calc
Author:<harish>
Version:0.1
date:4/12/17

'''


from __future__ import division
try:
  def cost():
    c=0
    cp=24.95
    d=40
    sp=3
    sp1=0.75
    n=int(raw_input("enter number of copies: "))
    if(n==1):
      c=c+cp*(d/100)*sp
    else:
      c=c+(cp*(d/100)*sp1*n)
    print "the wholesale cost is " + str(c)
  cost()
except Exception as e:
  print e