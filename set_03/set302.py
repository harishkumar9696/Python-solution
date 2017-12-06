'''
Name:set302.py 
Description: rotate
Author:<harish>
Version:0.1
date:06/12/2017
'''
def rotate_word(word,no):
    a=[]
    b=[]
    c=[]
    for i in word:
        a.append(ord(i))
    for i in a:
        b.append(i+no)  
    for i in b:
        c.append(chr(i))
    print c  
word=list(raw_input("Enter The word"))
no=int(raw_input("Enter the no by which u want to rotate:"))
rotate_word(word,no)