# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 00:53:27 2024

@author: suraj
"""

#******************operation on list i.e list comprehension**************
# append :  IT can add the element  at last of the list
lst = []
for num in range(0, 20):
    lst.append(num)
print(lst)
# o.p:-[0,1,2,3,……..,19]

############################################################
# List Comprehension':-
'''1.We can write same methods using the list comprehension
2.Comprehension can reduce the line of the codes
3. systax = [write the lines of for condition]
# 4. Comprehension:-comprehension in the python orovides us with a short and concise way to construt
			 New sequence using the sequence with have been alredy  defined'''
# Methodes using the list comprehension
#IMP One Question for In interview

lst = [num for num in range(0, 20)]
print(lst)  # o.p:-[0,1,2,3,……..19]

############################################################
#Capitalize: -every first letter will be captalize of word call the methood along with the name of the list
#Example: -
name = ['dada', 'kaka', 'mama']
lst = [name.capitalize() for name in name]
print(lst)  # o.p:- ['Dada', 'Kaka', 'Mama']

###########################################################
#list comrehension with 'if' statement
# 'if' should be right side of the for loop. write the  code in  the suitable format we use the it statement  and another way is also present i.e in one line


def is_even(num):
    return num % 2 == 0


lst = [
     num
     for num in range(10)
     if is_even(num)
     ]
print(lst)
# o.p:- [0,2,4,6,8]

###########################################################
#Above code are written in the one line by using the  list comprehension

def is_even(num):
    return num % 2 == 0


lst = [num for num in range(10) if is_even(num)]
print(lst)  # o.p:-[0,2,4,6,8]

#####################################
#list comrehension to print a particular digit
lst = [f"{x}{y}"
      for x in range(3)
      for y in range(3)
      ]
print(lst)  # o.p:- ['00', '01', '02', '10', '11', '12', '20', '21', '22']
# can print the number in the particular digit . it has another part also as like the nested for loop

######################################################
#1)set comprehension: -
# set comprehension are pretty similar to list comprehension .The only Difference between them is that set comprehension are  in the curly bracket {}. Not allow the duplicate element. It give the result in the form of set only Key are index of the number
lst={x
     for x in range(3)
     }
print(lst)  # o.p:- {0, 1, 2}

########################################################
#2) Dictionary comprehension
# give the result in the form of the dictionary it give the key as well as value we process on the value rather than the key component
# syntax:- output_dict={Key:value or(key,value) in iterable if(key,value statisfy thi condition)}
dict={x: x*x
     for x in range(3)
     }
print(dict)  # o.p:- {0: 0, 1: 1, 2: 4}

##############################################################
#Generator
# It is another way of creating the iterator in the simple way where  it uses the keyword “yield” instead of returing it in a defined function genterated are implemented using the a function
gen=(x
     for x in range(3)
     )
print(gen)  # gen is the object
for num in gen:
    print(num)  # o.p:-0,1,2
# (): object

###############################################################
#Next
# it give the line by line output generted object:- generated function return a generator object Generated object are used either by calling the next method on the generator object  or using the genertoor object in the “for in loop”
gen=(x
     for x in range(3)
     )
next(gen)  # o.p:-0

#########################################################
gen=(x for x in range(3))
next(gen)  # o.p:-0
next(gen)  # o.p:-1
# the last output give the answer as 1

#####################################################
gen=(x for x in range(3))
next(gen)  # o.p:-0
next(gen)  # o.p:-1
next(gen)  # o.p:-2
next(gen)  # o.p:-error out of the loop

######################################################
# Yield:-access the multipele value by using the yield
def range_even(end):
    for num in range(0, end, 2):
        yield num  # above are definition of the function
for num in range(6):
    print(num)  # o.p:-0,1,2,3,4,5

######################################################
#Now  next insted of the for loop
gen=range_even(16)
next(gen)  # o.p:-0
next(gen)  # O.p:- 2
next(gen)  # o.p:-4
next(gen)  # o.p:-6
next(gen)  # o.p:-8
# o.p:-8

######################################################
#Application of the generator
#Generator function are defined like a normal function but whenever it needs to generate a value
#It close so with the yield keyword rather that return
#If the body of a def contains yield the function automatically becomes a generator function
#1 chaining generator: - chain the various function
def length(itr):
    for ele in itr:
        yield len(ele)
def hide(itr):
    for ele in itr:
        yield ele*'*'
passwords=["not good", "given'm pass", "00100=100"]
for password in hide(length(passwords)):
    print(password)
# o.p:- ********
#** **********
#*********
# it can count the length of the password and print the * instend of the character

#####################################################
#Printing the list with index
#Here we can increment the index value with 1 becz of the index start with the 0 index It can make the space between the index value and list element It can print the elemnt of the list with there index value
lst=["milk", "egg", "bread"]
for index in range(len(lst)):
    print(f"{index+1} - {lst[index]}")
'''# o.p:- 1 - milk
2 - egg
3 – bread
'''
#######################################################
