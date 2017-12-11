'''
Name:set405.py 
Description: co ordinates
Author:<harish>
Version:0.1
date:11/12/2017
'''
class Coordinate(object):
  def __init__(self, x, y):
    self.x = x
    self.y = y

  def getX(self):
    # Getter method for a Coordinate object's x coordinate.
    # Getter methods are better practice than just accessing an attribute directly
    return self.x

  def getY(self):
    # Getter method for a Coordinate object's y coordinate
    return self.y

  def __str__(self):
    return '<' + str(self.getX()) + ',' + str(self.getY()) + '>'
  
  '''Add an eq method that returns True if coordinates refer to same point in the plane (i.e., have the same x and y coordinate).'''
  def eq(self,a,b):
    return (a==self.x and b==self.y)
  
a=int(raw_input("enter the x coordinate:"))
b=int(raw_input("enter the y coordinate:"))
obj=Coordinate(a,b)
print obj.__str__()
print obj.eq(5,6)