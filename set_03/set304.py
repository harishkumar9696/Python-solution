'''
Name:set304.py 
Description: perceentage of has_no_e
Author:<harish>
Version:0.1
date:06/12/2017
'''
def has_no_e(list1):
    with_e=[]
    without_e=[]
    for str in strlist:
        if 'e' in str:
            with_e.append(i)
        elif 'E' in str:
            with_e.append(i)
        else:
            without_e.append(i)
    original_len=float(len(list1))
    len_with_e=float(len(with_e))
    len_without_e=len(without_e)
    percentage=(len_without_e/original_len)*100
    print percentage
str=raw_input("Enter the string followed by space")
strlist=str.split(' ')
list1=[]
for i in strlist:
    list1.append(i)
print list1
has_no_e(list1)