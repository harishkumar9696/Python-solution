'''
Name:set402.py 
Description: calc
Author:<harish>
Version:0.1
date:11/12/2017
'''
#parent class      
class Person:
  def getgender(self):
    pass
    
#derived class    
class Male(Person):
  def getgender(self):
    print "Male"
    
#derived class     
class Female(Person):
  def getgender(self):
    print "Female"


a=raw_input("enter the gender as m or f:")
if a=="m":
# object 
  obj=Male()
  obj.getgender()
elif a=="f":
  obj=Female()
  obj.getgender() 