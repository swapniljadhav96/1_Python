# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 00:47:28 2024

@author: suraj
"""

"""------------------------------------------Exception handling-----------------------------"""
# The error signifies a sitution that mostly happen  due to the absenceof the system resoursethe exception are the issue that can be appear at run time and compile time it majority occure in tha code or program authoriesd by the devloper
# Exception are sovled by the try and exception block performallity it can make the code less  error free
try:
    print(5/0)
except ZeroDivisionError:
    print(" you cannot dive by zero")
# o.p:- you cannot dive by zero

########################################################
# Taking the input from  the user  take the correct iinput and avilablity of the program
print("give me two number and i will solve it")
print("enter the 'q' to quit")
while True:
    first_num = input("enter the 1st num")
    if first_num == 'q':
        break
    second_num = input("enter the 2nd num")
    if second_num == 'q':
        break
    answer = int(first_num)/int(second_num)
    print(answer)

########################################################
# Handling  the filenotfound error exception the file are not are avilable
filename = 'alice.txt'
with open(filename, encoding='utf-8') as f:
    content = f.read()
#########################################################
# it is solve by using the try and exception block
filename = 'alice.txt'
try:
    with open(filename, encoding='utf-8') as f:
        content = f.read()
except FileNotFoundError:
    print("sorry the file not found")
