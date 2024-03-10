# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 10:47:13 2024

@author: suraj
"""

#**************************lambda function**************************
'''#Lambdaa function/Anonymous function:-
1.	Lambda function is a small anonymous function 
2.	A lambda  function can take any number of argument ,but can only have one expression
3.	The power of lambda is better show when you use them as an anonymous function is required for a small or short period of time
4.	Space complexity :- reduce because occupy the explicitly memory
'''
#Simple function:-
def add(a,b,c):
    sum=a+b+c
    return sum
print(add(4,5,6))			#o.p:-15

# lambda function
add=lambda a,b,c:a+b+c
add(4,5,6)				#o.p:-15

####################################################
# simple function 
def mult(a,b,c):
    mul=a*b*c
    return mul
print(mult(4,5,6))
# positional parametr:-by using the lambda fun
mult=lambda a,b,c: a*b*c
mult(4,5,6)
#o.p:-120

#################################################
#arbetary fun:- we can pass n number  of parameter
val=lambda *args:sum(args)
val(1,2,3,4,5,6)
#o.p:-21

##################################################
#  *args normal fun
def myfun(*args):
    for i in args:
        print(i)					#o.p:- hello python how  are you
myfun("hello","python","how ","are","you")

#lambda
myfun=lambda *args:args
print("hello","python","how ","are","you")    
 #o.p:- hello python how  are you

##################################################
#simple program
def person(name,*data):
    print(name)
    print(data)
person("navin",28,"mumbai",12345678)
#o.p:- navin 28 mumbai 12345678
#lambda
person=lambda *data,name: data
print("navin",28,"mumbai",12345678)
#o.p:- navin 28 mumbai 12345678
######################################################
#****sir ne quetion vichar la hota oral la *****
#taking the input from the user
x=int(input("enter the number:"))
def add():
    y=x+5
    print(y)
add()

# passsing the x as the postional arrugment
def add(x):
    y=x+5
    print(y)
add(10)

#lambda with positional  aregument as x
x=int (input("enter the number:"))
add=lambda x:x+5
add(x)

#lambda without positional argument as x
x=int (input("enter the number:"))
add=lambda :x+5
add()

################################
# **kwargs passing the key word as the argument
def person(name,**data):
    print(name)
    print(data)
person(name="navin",age=28,place="mumbai",mob=12345678)
#o.p:- navin
{'age': 28, 'place': 'mumbai', 'mob': 12345678}


#lambda
person=lambda **data:data
person(name='navin',age=28,place="mumbai",mob=12345678)
#o.p:- navin
#{'age': 28, 'place': 'mumbai', 'mob': 12345678}

###########################################################
#** dictionary like
def person(name,**data):
    print(name)
    for i,j in data.items():
        print(i,j)
person(name="navin",age=28,place="mumbai",mob=12345678)
#o.p:- ['navin', 28, 'mumbai', 12345678]

# lambda fun
person=lambda **data:[(j)for i,j in data.items()]
person(name='navin',age=28,place='mumbai',mob=12345678)
#o.p:- ['navin', 28, 'mumbai', 12345678]

##########################################################
#call the as direct value
val =lambda **data:sum(data.values())
val(a=1,b=2,c=3,d=5)
#o.p:- 11

#########################################################
#take the square of the list parameter lambda function in the list industry imp
lst1=[1,2,3,4,5,6,7]
sqr=lambda lst1:[i**2 for i in lst1]
print(sqr(lst1))
#output:-[1, 4, 9, 16, 25, 36, 49]

