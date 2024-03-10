# -*- coding: utf-8 -*-
"""
Created on Sat Mar  9 23:32:20 2024

@author: suraj
"""

# Flow of Control Using
# **If Statements**
# **Comparison Operators**
'''Before exploring if statements we need to discuss comparison operators. These are operators that return Boolean values. They are key to the conditional elements of flow of control statements such as if. A comparison operator is an operator that performs some form of test and returns True of False.
Note that indentation, this is very important in Python; indeed, layout of the code is very, very important in Python. Indentation is used to determine how one piece of code should be associated with another piece of the code '''
# Example
num = int(input('Enter a number: '))
if num > 0:
print(num)  # o.p:- it  gives an error due to indentation

#######################################
# Now let us give the indentation
num = int(input('Enter a number: '))
if num > 0:
    print(num)  # o.p:- it give the user input to and check with it
# o.p:-num=5
# o.p=5
#######################################
# Else in an If Statement
num = int(input('Enter yet another number: '))
if num < 0:
    print('Its negative')
else:
    print('Its not negative')

# *****************************************************************************
# **The Use of if_elif_else**
savings = float(input("Enter how much you have in savings: "))
if savings == 0:
    print("Sorry no savings")
elif savings < 500:
    print('Well done')
elif savings < 1000:
    print('Thats a tidy sum')
elif savings < 10000:
    print('Welcome Sir!')
else:
    print('Thank you')
# *********************************************************************
# **Iteration/Looping**
# **While Loop**
# The while loop exists in almost all programming languages and is used to iterative (or repeat) one or more code statements as long as the test condition (expression) is True
# Example
count = 1
print('Starting')
while count <= 10:
    print(count)
    count += 1
    # o.p:- Starting 12345678910
# *******************************************************************************
# For Loop:- Loop over a set of values in a range
# Example
print('Print out values in a range')
for i in range(2, 10):
    print(i)
    print('Done')
# o.p:- Print out values in a range
'''2Done
3Done
4Done
5Done
6Done
7Done
8Done
9Done
Taking the input from the user
'''
######################################
# Example
print('Only print code if all iterations completed')
num = int(input('Enter a number to check for: '))
for i in range(0, 16):
    if i == num:
        break
    print(i)
    print('Done')
# o.p:-Only print code if all iterations completed
'''Enter a number to check for: 2
0Done
1Done
'''
######################################
# Now use an 'anonymous' loop variable
for _ in range(0, 10):
    print('.', end='')
    print()
# o.p:- .
'''.
.
.
.
.
.
.
.
.'''
################################################
for _ in range(0, 10):
    print('.', end='')  # o.p:- ..........
# ******************************************************************************
# **Break Loop Statement**
# With the break statement we can stop the loop before it has looped through all the items:
print('Only print code if all iterations completed')
num = int(input('Enter a number to check for: '))
for i in range(0, 6):
    if i == num:
        break
    print(i, ' ', end='')
print('Done')
# o.p:- Only print code if all iterations completed
'''Enter a number to check for: 2
0  1  Done'''

#################################################
# location of print is changed
for i in range(0, 6):
    if i == num:
        break
    print(i, ' ', end='')
    print('Done')
'''#o.p:- 0  Done
1  Done'''

##############################################
# Even number logic:-
for i in range(0, 10):
    #print(i, ' ', end='')
    if i % 2 == 1:
        continue
        print('hey its an even number')
        print('we love even numbers')
print('Done')
# o.p:- 0  1  2  3  4  5  6  7  8  9  Done
# *******************************************************************************
# **The continue Statement**
# **continue**
# With the continue statement we can stop the current iteration of the loop, and continue with the next:
# Example
# Do not print banana:
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        continue
    print(x)
#o.p:- apple
# cherry
# ********************************************************************************
# **The range() Function**
# To loop through a set of code a specified number of times, we can use the range() function, The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and ends at a specified number.
# Example
# Using the range() function:
for x in range(6):
    print(x)
'''#o.p:- 
0
1
2
3
4
5
'''
#######################
# Note that range(6) is not the values of 0 to 6, but the values 0 to 5.
# The range() function defaults to 0 as a starting value, however it is possible to specify the starting value by adding a parameter: range(2, 6), which means values from 2 to 6 (but not including 6)
# Example
# Using the start parameter:
for x in range(2, 6):
    print(x)
'''#o.p:- 2
3
4
5'''
#####################################
# The range() function defaults to increment the sequence by 1, however it is possible to specify the increment value by adding a third parameter: range(2, 30, 3):
# Example
# Increment the sequence with 3 (default is 1):
for x in range(2, 30, 3):
    print(x)
#o.p:- 2
'''5
8
11
14
17
20
23
26
29
'''
# ******************************************************************************
# **Nested if_else :-**
# Write python code using nested if else.so as to check height as well as so as to allow for roller coster
# example
print("Welcome to the roller coaster")
height = int(input("Please enter your height"))
age = int(input("Please enter your age "))
if height >= 120:
    print("you can ride the roller coaster")
    if age <= 18:
        print("your ticket will be 7$")
    else:
        print("your ticket will be 12$")
else:
    print("Sorry,you need to grow taller before you can ride")
'''#o.p:-
Welcome to the roller coaster
Please enter your height23
Please enter your age 18
Sorry,you need to grow taller before you can ride
'''
# ******************************************************************************
# Nested if-elif statment :-
# Write python code using   if elif.so as to check height as well as so as to allow for roller coster, using elif further you check age category and charge ticket accordingly
# Example
print("Welcome to the roller coaster")
height = int(input("Please enter your height"))
if height >= 120:
    print("you can ride the roller coaster")
    age = int(input("Please enter your age "))
    if age < 12:
        print("your ticket will be 5$")
    elif age > 12 and age < 18:
        print("your ticket will be 7$")

    elif age > 18:
        print("your ticket will be 12$")
else:
    print("Sorry,you need to grow taller before you can ride")
'''#o.p:-
Welcome to the roller coaster
Please enter your height85
Sorry,you need to grow taller before you can ride
#we can put the input as per our requirements so the  answer is change so if the input are change
'''
# *******************************************************************************
# Iterators
numbers = [1, 4, 6]
value = numbers.__iter__()
item1 = value._next__()
print(item1)  # o.p:-1
item2 = value.__next__()
print(item2)  # o.p:-4
item3 = value.__next__()
print(item3)  # o.p:-6

################################
num2 = [6, 8, 2]
val = iter(num2)
itm1 = next(val)
print(itm1)  # o.p:-6
itm2 = next(val)
print(itm2)  # o.p:-8
itm3 = next(val)
print(itm3)  # o.p:-2
