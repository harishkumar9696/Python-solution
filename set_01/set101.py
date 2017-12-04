'''
Name:set101.py 
Description: Largest odd number 
Author:<harish>
Version:0.1
date:4/12/17

'''
print("enter three odd numbers ")
a=raw_input("enter the first number  ")
b=raw_input("enter the second number ")
c=raw_input("enter the third number ")
a=int(a)
b=int(b)
c=int(c)


if(a%2!=0 and b%2!=0 and c%2!=0):  
    if(a>b and a>c):
        print(a," is large")
    elif(b>a and b>c):
        print(b," is large")
    else:
        print(c," is large")

elif(a%2!=0 and b%2!=0 and c%2==0):
    print (c," is not odd number")
    if(a>b):
        print(a," is largest odd number")
    else:
        print(b," is largest odd number")


elif(a%2==0 and b%2!=0 and c%2!=0):#when b and c are odd numbers
    print (a," is not odd number")
    if(b>c):
        print(b," is largest odd num")
    else:
        print(c," is largest odd num")


elif(a%2!=0 and b%2==0 and c%2!=0):#when a and c are odd numbers
    print (b," is not odd number")    
    if(a>c):
        print(a," is largest odd num")
    else:
        print(c,"is largest odd number")


elif(a%2==0 and b%2==0 and c%2!=0):#when c alone is an odd number
    print (a,b," is not odd number")
    print(c," is largest odd num")

elif(a%2!=0 and b%2==0 and c%2==0):#when a alone is an odd number 
    print (b,c," is not odd number")
    print(a," is largest odd num")

elif(a%2==0 and b%2!=0 and c%2==0):#when b alone is an odd number
    print (c,a," is not odd number")
    print(c," is largest odd num")

else:#all are even numbers
    print("not odd number")