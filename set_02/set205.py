'''
Name:set205.py 
Description: sum of integers
Author:<harish>
Version:0.1
date:4/12/17

'''
try:
  def sumDigits(a):
    sum=0
    for i in a:
      if(i.isdigit()):
        sum=sum+int(i)
    print "sum is "+str(sum)
  a=raw_input("enter a combination of string and numbers")
  sumDigits(a)
except Exception as e:
  print e 