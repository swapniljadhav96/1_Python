# -*- coding: utf-8 -*-
"""
write python code to find fibbonacy series

@author: Dell
"""

def fibbo(n):
        lst=[]
        previous=0
        current=1
        lst.append(current)
        for i in range(n-1):
            previous,current=current,previous+current 
            lst.append(current)
        return lst

        
print(fibbo(8))


def fibbo(n):
    lst=[]
    previous=0
    current=1
    lst.append(current)
    for i in range(n-1):
        previous,current=current,previous+current
        lst.append(current)
    return lst    
        

print(fibbo(8))
