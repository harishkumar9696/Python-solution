
'''
Name:set305.py 
Description: forbidden
Author:<harish>
Version:0.1
date:06/12/2017
'''
def avoids(string,forbidden):
    for i in forbidden:
        if i in string:
            return False
    else:
        return True
string="hello"
forbidden=['v','w','x','y','z']
print avoids(string,forbidden)