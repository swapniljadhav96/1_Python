# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 00:45:08 2024

@author: suraj
"""

# print the ticket number by random
from random import randrange
min_num = 1
max_num = 49
num_nums = 6
ticket_nums = []
for i in range(num_nums):
    # Generate the number that is not in the list
    rand = randrange(min_num, max_num+1)
    while rand in ticket_nums:
        rand = randrange(min_num, max_num+1)
    # Add the distinct number to the ticket
    ticket_nums.append(rand)
ticket_nums.sort()
for n in ticket_nums:
    print(n, end="")


"""------------write the python code remove outlier--------"""
# doble sort 1 2
values = [89, 195, 7, 4, 12, 23]
retval = sorted(values)  # 1sort


def removeoutliers(data, num_outliers):
    retval = sorted(data)  # sort2
    for i in range(num_outliers):
        retval.pop(-1)
    return retval


# it remove the last three number from the list ie we  pass the 3 value
removeoutliers(values, 3)

# outlier:- remove the last element or bigger number

# sort at 1
values = [89, 195, 7, 4, 12, 23]
retval = sorted(values)  # 1sort


def removeoutliers(data, num_outliers):
   # retval=sorted(data)
    for i in range(num_outliers):
        retval.pop(-1)
    return retval


removeoutliers(values, 3)


"""
write python code that determine whether or not 
a password strong.We define strong password if it follows
Following conditions
1.it must have at least 8 charecters
2.It must have at least one upper case letter
3.one lower case letter
"""


def checkPassword(password):
    has_upper = False
    has_lower = False
    has_num = False
# check each character in the password and see which
# requirement meets
    for ch in password:
        if ch >= "A" and ch <= "Z":
            has_upper = True
        elif ch >= "a" and ch <= "z":
            has_lower = True
        elif ch >= "0" and ch <= "9":
            has_num = True
    if len(password) >= 8 and has_upper and has_lower and has_num:
        return True
    else:
        return False


p = input("Enter a password  :")
if checkPassword(p):
    print("Strong password")
else:
    print("Weak password")
