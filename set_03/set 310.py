'''
Name:set310.py 
Description: anagram
Author:<harish>
Version:0.1
date:06/12/2017
'''
def is_anagram(str1, str2):
  s_str1=sorted(str1)
  s_str2= sorted(str2)
  if s_str1==s_str2:
    print ("It is an anagram")
  else:
    print ("It is not an anagram")
str1=raw_input('enter the first string')
str2=raw_input('enter the second string')
is_anagram(str1, str2)