# -*- coding: utf-8 -*-
"""
Created on Mon Aug 29 19:05:38 2022

@author: Dell
"""

def prime_num(num):
    for i in range(2,num):
        if (num%i==0):
            return "The number is not prime"
            break
  
    return "The number is prime"

print(prime_num(11))

# Prime determination method
def prime(num1):
    
        for i in range(2,num1):
            if (num1%i==0):
                return "The number is not prime"
                break
        
        return "The no is prime"
        
print(prime(11))

