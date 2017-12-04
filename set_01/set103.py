'''
Name:set103.py 
Description: largest odd number
Author:<harish>
Version:0.1
date:4/12/17

'''
list=[]
list2=[]
counter=0
while counter<10 :
    num=raw_input("enter numer or q to quit")
    if num== 'q':
        break
    else:
        list.append(int(num))
        counter=counter+1
print list
for i in list:
    if i%2<>0:
        list2.append(i)
    else:
        print "The odd numbers are "

print list2
print max(list2)

