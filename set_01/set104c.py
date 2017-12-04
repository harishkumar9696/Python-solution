'''
Name:set104c.py 
Description: calc
Author:<harish>
Version:0.1
date:4/12/17

'''

from __future__ import division
try:
  st=6.52
  t1=st*60
  easy=2
  tempo=3
  tot_time=((easy*(8/15))+(tempo*(7/12)))*60
  time=float((tot_time+st)/60)
  print time
except Exception as e:
  print e