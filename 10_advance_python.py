# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 10:32:00 2024

@author: suraj
"""

# $Enumerate
'''1.enumerate methods add a counter to an iterable and returns if in a from of enumerating object
2. this enumerate object can be used drirectly for loops or converted into a list of tuples using the list function
3.Syntax:- enumerate(iterable ,start=0)
Iterable:- any object that support iteration
Start:- the index from  which the counter is to be started ,by default it is 0
'''
# same code can be implemented using enumerate:-
import hashlib
import copy
from itertools import product
from itertools import permutations
from itertools import combinations
from itertools import repeat
import itertools
from itertools import count
from itertools import zip_longest
lst = ['milk', 'egg', 'bread']
for index, item in enumerate(lst, start=1):
    print(f"{index} {item}")
'''#o.p:- 1 - milk
2 - egg
3 – bread
'''
############################################################
# zip:-Use of zip function with the mis-match function
name = ['dada', 'mama', 'kaka']
info = [9850, 6032, 9785]
for nm, inf in zip(name, info):
    print(nm, inf)
'''#o.p:- dada 9850
mama 6032
kaka 9785
'''
#########################################################
# Use of zip function with mis match list
name = ['dada', 'mama', ' kaka', 'baba']
info = [9850, 632, 9785]
for nm, inf in zip(name, info):
    print(nm, inf)
'''#o.p:- dada 9850
mama 632
 kaka 9785  '''
# It will not display excess mismatch item in name I .e. baba

##############################
# zip_longest :- It print  the values of iterables alternately in sequence. If one of the iterables is printed fully the remaining values are filled by the values assigned  to fill value parameter
name = ['dada', 'mama', 'kaka', 'baba']
info = [9850, 6032, 3297]
for nm, inf in zip_longest(name, info):
    print(nm, inf)
'''#o.p:- dada 9850
mama 6032
kaka 3297
baba None
'''
###########################################################
# use of fill value instead None
name = ['dada', 'mama', 'kaka', 'baba']
info = [9850, 6032, 3297]
for nm, inf in zip_longest(name, info, fillvalue=0):
    print(nm, inf)
'''#o.p:- dada 9850
mama 6032
kaka 3297
baba 0
'''
##########################################################
# use of all():- if all the values are true then it will produce output(means the not the null or 0 present)
lst = [2, 3, 6, 8, 9]
if all(lst):
    print('all values are true')
else:
    print('Useless')
# o..p:- all values are true

#########################
lst = [2, 3, 0, 8, 9]
if all(lst):
    print('all values are true')
else:
    print('Useless')
#o.p:- Useless

#################################
# use of any()
# Something value are present in the list means all the value are not same value are null and come having some value
lst = [0, 0, 0, 8, 0]
if any(lst):
    print('It has some value')
else:
    print('Useless')
# o.p:- It has some value

##########################################################
# use of any
lst = [0, 0, 0, 0, 0]
if any(lst):
    print('It has some value')
else:
    print('Useless')
# o.p:-Useless

#########################################################

# count() :- it is used I deep learing()
counter = count()
print(next(counter))  # 0
print(next(counter))  # 1
print(next(counter))  # 2
'''#o.p:-0
1
2
'''
##########################################################
# Now let us start from 1
counter = count(start=1)
print(next(counter))
print(next(counter))
print(next(counter))
'''#o.p:-1
2
3
'''
#############################################################
# cycle()
# suppose you have repeated tasks to be done, in the certain time then you can use this method
instructions = ("Eat", "code", "sleep")
for instruction in itertools.cycle(instructions):
    print(instruction)
'''  #o.p:- Eat
Code
Sleep
Eat
Code
sleep
Eat
Code
sleep
Eat
Code
Sleep……………………………
'''
#################################################################
# repeat():-It can repeat the task as you can give the task input
for msg in repeat("keep patience", times=3):
    print(msg)
'''#o.p:- keep patience
keep patience
keep patience
'''
##############################################################
# group():-Group are the variable not a  special key world. It can group the listed element
player = {'john', 'jain', 'sumit'}
for group in combinations(player, 2):
    print(group)
'''#o.p:- ('jain', 'sumit')
('jain', 'john')
('sumit', 'john')
'''
############################################################
# group are the variable not the special key word
player = {'john', 'jain', 'sumit'}
for x in combinations(player, 2):
    print(x)
'''#o.p:- ('jain', 'sumit')
('jain', 'john')
('sumit', 'john')
'''
############################################################
# combinations()
players = ['John', 'Jani', 'Janardhan']
for i in combinations(players, 2):
    print(i)
'''#o.p:- ('John', 'Jani')
('John', 'Janardhan')
('Jani', 'Janardhan')
'''
#####################################################
players = ['John', 'Jani', 'Janardhan']
for seat in permutations(players, 2):
    print(seat)
'''#o.p:-('John', 'Jani')
('John', 'Janardhan')
('Jani', 'John')
('Jani', 'Janardhan')
('Janardhan', 'John')
('Janardhan', 'Jani')
'''
#######################################################
# product()
team_a = ['Rohit', 'Pandya', 'Bumrah']
team_b = ['virat', 'Manish', 'Sami']
for pair in product(team_a, team_b):
    print(pair)
'''#o.p:-('Rohit', 'virat')
('Rohit', 'Manish')
('Rohit', 'Sami')
('Pandya', 'virat')
('Pandya', 'Manish')
('Pandya', 'Sami')
('Bumrah', 'virat')
('Bumrah', 'Manish')
('Bumrah', 'Sami')
'''
##########################################################
age = [27, 17, 21, 19]
adults = filter(
    lambda age: age >= 18,
    age
)
print([age for age in adults])
#o.p:- [27, 21, 19]

###########################################################
# shallow copy and deep copy
# Copy an Object in Python
# Copy using = operator
old_list = [[1, 2, 3], [4, 5, 6], [7, 8, 'a']]
new_list = old_list
new_list[2][2] = 9
print('Old List:', old_list)
print('ID of Old List:', id(old_list))
# 2766531782016
print('New List:', new_list)
print('ID of New List:', id(new_list))
# same-2766531782016

# As you can see from the output both variables
# old_list and new_list shares the same id i.e 140673303268168.

#################################################
# Essentially, sometimes you may want to have the original values unchanged and only modify the new values or vice versa.In Python, there are two ways to create copies:
# Shallow Copy
# Deep Copy
# We use the copy module of Python for  shallow and deep copy operations.
# Suppose, you need to copy the compound list say x.

x = [1, 2, 3]
copy.copy(x)  # Here, the copy() return a shallow copy of x.
copy.deepcopy(x)  # Similarly, deepcopy() return a deep copy of x.
# A shallow copy creates a new object
# which stores the reference of the original elements.
old_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
new_list = copy.copy(old_list)

print("Old list:", old_list)
print("New list:", new_list)
# This means it will create new and independent object with same content.
# To verify this, we print the both old_list and new_list.
# To confirm that new_list is different from old_list
# we try to add new nested object to original and check it.
old_list = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
new_list = copy.copy(old_list)
old_list.append([4, 4, 4])
print("Old list:", old_list)
print("New list:", new_list)
# In the above program, we created a shallow copy of old_list. The new_list contains references to original nested objects stored in old_list. Then we add the new list i.e [4, 4, 4] into old_list. This new sublist was not copied in new_list.

##########################################################
# However, when you change any nested objects in old_list, the changes appear in new_list.
old_list = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
new_list = copy.copy(old_list)
old_list[1][1] = 'AA'
print("Old list:", old_list)
print("New list:", new_list)

# n the above program, we made changes to old_list i.e old_list[1][1] = 'AA'.
# Both sublists of old_list and new_list at index [1][1] were modified. This is becauses, both lists share the reference of same nested objects.

############################################################
# Deep Copy
# A deep copy creates a new object and  recursively adds the copies of nested objects present in the original elements.
old_list = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
new_list = copy.deepcopy(old_list)
print("Old list:", old_list)
print("New list:", new_list)

# However, if you make changes to any nested objects in original object old_list,  you’ll see no changes to the copy new_list.

old_list = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
new_list = copy.deepcopy(old_list)
old_list[1][0] = 'BB'
print("Old list:", old_list)
print("New list:", new_list)
# In the above program, when we assign a new value to old_list, we can see only the old_list is modified. This means, both the old_list and the new_list are independent.
lst1 = [1, 2, [3, 4], 5]  # using shallow copy
lst2 = copy.copy(lst1)
print(
    f"The id of lst1 :{id(lst1)} and value is {lst1}and id of lst2:{id(lst2)} and the value is {lst2}")
"""
The id of lst1 :2335553487232 and value is [1, 2, [3, 4], 5]and id of lst2:2335553755904 and the value is [1, 2, [3, 4], 5]
"""
lst1 = [1, 2, [3, 4], 5]  # using shallow copy
lst3 = copy.deepcopy(lst1)
print(
    f"The id of lst1 :{id(lst1)} and value is {lst1}and id of lst2:{id(lst3)} and the value is {lst3}")
"""
The id of lst1 :2335553487232 and value is [1, 2, [3, 4], 5]and id of lst2:2335552727424 and the value is [1, 2, [3, 4], 5]
"""
#####################################################
# importing "copy" for copy operations

# initializing list 1
li1 = [1, 2, [3, 5], 4]

####################################################
# using deep copy to deep copy
li2 = copy.deepcopy(li1)

######################################################
# original elements of list
print("The original elements before deep copying")
for i in range(0, len(li1)):
    print(li1[i], end=" ")

 ####################################################
# adding and element to new list
li2[2][0] = 7

####################################################
# Change is reflected in l2
print("The new list of elements after deep copying ")
for i in range(0, len(li1)):
    print(li2[i], end=" ")

 #####################################################
# Change is NOT reflected in original list as it is a deep copy
print("The original elements after deep copying")
for i in range(0, len(li1)):
    print(li1[i], end=" ")
########################################
# Shallow copying on the contrary any change made in copied object same change is reflected in original object
# importing "copy" for copy operations
li1 = [1, 2, [3, 5], 4]		# initializing list 1
li2 = copy.copy(li1)		# using copy to shallow copy
# original elements of list
print("The original elements before shallow copying")
for i in range(0, len(li1)):
    print(li1[i], end=" ")

 #####################################################
# adding and element to new list
li2[2][0] = 7

# checking if change is reflected
print("The original elements after shallow copying")
for i in range(0, len(li1)):
    print(li1[i], end="")

    ####################################################
# unpacking of dictinary
friends = {
    "Dale": 9850,
    "male": 6034
}
contacts = {
    "dada": 8530,
    "mama": 5286
}
contacts.update(friends)
print(contacts)

####################################
# pipe operator
friends = {"Satish": 99021,
           "Ram": 97603
           }
sham = {"sham": 85305}
all_friends = friends | sham
print(all_friends)

#############################
num = 0


def change():
    num = 1


change()
print(num)
# output will be 0
# In the same way we can not access outside of function  the value of variable declared inside the function
num = 0


def change(x):
    x = 1


change(x)
print(num)  # it will show an error

########################################
# use the admine user
users = ["admine", "employee", "manager", "worker", "staff"]
for user in users:
    if user == "admin":
        print("hello admin ,would you like to see the status report")
    elif user == "employee":
        print("hello employe")
    elif user == "manager":
        print("hello manager")
    elif user == "worker":
        print("hello worker")
    else:
        print("hello staff")

#####################################################
# check the new user and old user
current_user = ["ali", "ahemd", "fahad", "aun", "rana"]
new_users = ["ali", "rana", "bilai", "huzi", "dula"]
for new_user in new_users:
    if new_user in current_user:
        print("person will need to enter  a new uersname")
        break
    else:
        print("saying that the username is avilable")
        break

##########################################################
# Hash code generation:- save the password in the form of hash code and check the user password and previous password are correct
hashlib.sha256("Gaurav@1234".encode('utf-8')).hexdigest()
'778d4ce2dfb7063981a67be5ba7955ba063c3319760bd3a0d2a85f5d15a594de'
len(hashlib.sha256("Gaurav@1234".encode('utf-8')).digest())
# 32 bit processor hashlib.sha256
############################################
hashlib.sha512("Gaurav@1234".encode('utf-8')).hexdigest()
'778d4ce2dfb7063981a67be5ba7955ba063c3319760bd3a0d2a85f5d15a594de'
len(hashlib.sha512("Gaurav@1234".encode('utf-8')).digest())

# 64 bit processor hashlib.sha512
