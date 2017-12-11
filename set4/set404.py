'''
Name:set404.py
Description: stars
Author:<harish>
Version:0.1
date:11/12/2017
'''
def nonrecursive():
  print "non-recursive"
  i=1
  j=7
  while i<=7:
    '''printing the pattern using non-recursive function'''
    if i!=4:
      print((j*' ')+i*'**')
    j=j-1
    i=i+1
nonrecursive()