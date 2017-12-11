'''
Name:set401.py 
Description: Shape
Author:<harish>
Version:0.1
date:
'''
class Shape:
  def area(self):
   print "the default area of shape is 0" 

#derived class    
class Square(Shape):
  def __init__(self,l):
    self.a=l
  #area calculation  
  def area(self):
    b=self.a*self.a
    return b

'''object'''    
obj=Square(5)
c=obj.area()
print (c)