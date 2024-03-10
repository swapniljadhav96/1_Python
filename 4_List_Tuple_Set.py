# -*- coding: utf-8 -*-
"""
Created on Sat Mar  9 23:56:04 2024

@author: suraj
"""
#Python Collection Types
#**Tuples** 
'''A Tuple represents a collection of objects that are ordered and immutable (cannot be modified).
Syntax:- ( )
'''
#####################################
#**Lists**
'''Lists hold a collection of objects that are ordered and mutable (changeable), they are indexed and allow duplicate members.
Syntax :- [ ]
'''
#####################################
#**Sets**
'''Sets are a collection that is unordered and unindexed. They are mutable (changeable) but do not allow duplicate values to be held.
Syntax :- {}
'''
####################################
#**Dictionary**
'''A dictionary is an unordered collection that is indexed by a key which references a value. The value is returned when the key is provided.
Syntax :-{key : value}
'''
#***************************************************************************
#opertion on the tuple
#1.Creating Tuples
tup1 = (1, 3, 5, 7)

###############################################
#2.Accessing Elements of a Tuple
print(f'tup1[0]:\t{tup1[0]}')
print('tup1[1]:\t', tup1[1])
print('tup1[2]:\t', tup1[2])
print('tup1[3]:\t', tup1[3])
'''#o.p :- tup1[0]:	1
tup1[1]:	 3
tup1[2]:	 5
tup1[3]:	 7
'''
#############################################
#3.Tuples Can Hold Different Types
tup2 = (1, 'John',  True, -23.45)
print(tup2)
#o.p:- (1, 'John', True, -23.45)

#############################################
#4.Iterating Over Tuples
tup3 = ('apple', 'orange', 'plum', 'apple')
for x in tup3:
   print(x)
'''#o.p:- apple
orange
plum  apple
'''
#################################################
#Tuple Related Functions
#1.You can also find out the length of a Tuple
len(tup3)
#o.p:-4

#################################################
#2.You can count how many times a specified value appears in a Tuple 
tup4 = ('apple', 'orange', 'plum', 'apple', 'apple')		# Tuples allow duplicates;
tup4.count('apple')
#o.p:-3

##############################################
#3.You can also find out the (first) index of a value in a Tuple:
print(tup4.index('apple'))		#o.p:-0
print(tup4.index('plum'))		#o.p:-2

##############################################
#4.Checking if an Element Exists
if 'orange' in tup3:
   print('orange is in the Tuple')			#o.p:- orange is in the Tuple

###############################################
#**Nested Tuples**
#Tuples can be nested within Tuples; that is a Tuple can contain, as one of its elements, another Tuple.
tuple1 = (1, 3, 5, 7)
tuple2 = ('John', 'Denise', 'Phoebe', 'Adam')
tuple3 = (42, tuple1, tuple2, 5.5)
print(tuple3)		#o.p:- (42, (1, 3, 5, 7), ('John', 'Denise', 'Phoebe', 'Adam'), 5.5)

#Note:-It is not possible to add or remove elements from a Tuple; they are immutable.

#********************************************************************************
#**Lists
#Lists are mutable ordered containers of other objects.
################################################################################
#opertion on the list
#1.Creating Lists
lst1 = ['John', 'Paul', 'George', 'Ringo']		#o.p:- lst1 = ['John', 'Paul', 'George', 'Ringo']

#################################################
#2.As with Tuples we can have nested lists and lists containing different types of elements.
lst1 = [1, 43.5, True]
lst2 = ['apple', 'orange', 31]
root_list = ['John', lst1, lst2, 'Denise']
print(root_list)		#o.p:- ['John', [1, 43.5, True], ['apple', 'orange', 31], 'Denise']

#################################################
#3.Accessing Elements from a List
lst1 = ['John', 'Paul', 'George', 'Ringo']
print(lst1[-1])					#o.p:- Ringo
lst1[-1]						#o.p:- 'Ringo'
lst1[-2]						#o.p:- 'George'

################################################
lst1 = ['John', 'Paul', 'George', 'Ringo']
print('lst1[1]:', lst1[1])				#o.p:- lst1[1]: Paul
print('lst1[-1]:', lst1[-1])			#o.p:- lst1[-1]: Ringo
print('lst1[1:3]:', lst1[1:3])			#o.p:- lst1[1:3]: ['Paul', 'George']
print('lst[:3]:', lst1[:3])				#o.p:- lst[:3]: ['John', 'Paul', 'George']
print('lst[1:]:', lst1[1:])				#o.p:-lst[1:]: ['Paul', 'George', 'Ringo']

###############################################
#4.Adding to a List:- append()
lst1 = ['John', 'Paul', 'George', 'Ringo']
lst1.append('Pete')
print(lst1)					#o.p:-['John', 'Paul', 'George', 'Ringo', 'Pete']

###############################################
#6.You can also add all the items in a list to another list. There are several options
lst1 = ['John', 'Paul', 'George', 'Ringo', 'Pete']
print(lst1)					#o.p:- ['John', 'Paul', 'George', 'Ringo', 'Pete']

#5.extend():- to add the more than one element in the list
lst1.extend(['Albert', 'Bob'])			#here, we can use the extend()
lst1						#o.p:- ['John', 'Paul', 'George', 'Ringo', 'Pete', 'Albert', 'Bob']

#############################################
#6.Inserting into a List
#Sytanx:- list_name.insert(location _index_value,inserting_element_name )
a_list = ['Adele', 'Madonna', 'Cher']
print(a_list)					#o.p:- ['Adele', 'Madonna', 'Cher']
a_list.insert(1, 'Paloma')
print(a_list)					#o.p:-['Adele', 'Paloma', 'Madonna', 'Cher']
#******************************************************************************
#7.List Concatenation :- we can easily concatenate the list as like the concatenating the two string.
lst1 = [3, 2, 1]
lst2 = [6, 5, 4]
lst3 = lst1 + lst2
print(lst3)					#o.p:- [3, 2, 1, 6, 5, 4]
 
#############################################
#8.Removing from a List
another_lst = ['Gary', 'Mark', 'Robbie', 'Jason', 'Howard']
print(another_lst)			#o.p:- ['Gary', 'Mark', 'Robbie', 'Jason', 'Howard']
another_lst.remove('Robbie')
print(another_lst)			#o.p:- ['Gary', 'Mark', 'Jason', 'Howard']

#############################################
#9.The pop() Method
#It removes an element from the List; however, it differs from the remove() method in two ways: It takes an index which is the index of the item to remove from the list rather than the object itself.
lst6 = ['Once', 'Upon', 'a', 'Time']
print(lst6)		#o.p:- ['Once', 'Upon', 'a', 'Time']
print(lst6.pop(2))	#o.p:-a
print(lst6)		#o.p:-['Once', 'Upon', 'Time']

#############################################
#10.Inserting into a List 
a_list = ['Adele', 'Madonna', 'Cher']
print(a_list)				#o.p:-['Adele', 'Madonna', 'Cher']
a_list.insert(1, 'Paloma')
print(a_list)				#o.p:-['Adele', 'Paloma', 'Madonna', 'Cher']

#######################
#11.List Concatenation
list1 = [3, 2, 1]
list2 = [6, 5, 4]
list3 = list1 + list2			#here the 2 list are added
print(list3)				#o.p:- [3, 2, 1, 6, 5, 4]

##############################################
#12.clear removes all the elements from the list
lst=["cherry","banana","apple"]
lst.clear()
print(lst)

#*****************************************************************************
#13.**copy() method**
lst=["cherry","banana","apple"]
lst2=lst.copy()
print(lst2)				#o.p:- the same another list is made

############################################
# 14.Reverse  :-it is used to reveres the list
lst=["cherry","cherry","banana"]
lst.reverse()
print(lst)

###########################################
#15.sort() :-Sort the list alphabetically
lst=["cherry","orange","banana"]
lst.sort()
print(lst)

##########################################
#16.multiplying all the element from the list
lst=[1,23,12,3]
mul1=1
for i in lst:			# accessing the element from the list
    mul1=mul1*i
print(mul1)

###########################################
#Write a method that takes in an integer n ,then iterates through all the numbers from 0 to n,return the sum of numbers which are divisible by 5 or 7
lst=[1,2,5,7,14,55,45,21,49,8,9]
def return_sum(lst):
    sum=0
    for i in range(len(lst)):
        if(lst[i]%5==0 or lst[i]%7==0):
            sum=sum+lst[i]
    return sum

print(return_sum(lst))        

########################################













Set
Set operation
Creating a Set
Example 
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)				#o.p :- {'apple', 'pear', 'banana', 'orange'}
#####When run this code will show that apple is only added once to the set:

##############################################
#Accessing Elements in a Set
for item in basket:
   print(item)
#o.p:- apple
pear
banana
orange
##############################################
#Adding Items to set
basket = {'apple', 'orange', 'banana'}
basket.add('apricot')
print(basket)				#o.p:- {'apricot', 'apple', 'banana', 'orange'}

##############################################
#If you want to add more than one item to a Set you can use the update() method:
basket = {'apple', 'orange', 'banana'}
basket.update(['apricot', 'mango', 'grapefruit'])
print(basket)				#o.p:- {'apple', 'grapefruit', 'apricot', 'orange', 'mango', 'banana'}

#############################################
#Obtaining the Length of a Set
basket = {'apple', 'orange', 'apple', 'pear', 'orange','banana'}
print(len(basket))			#o.p:- 4

############################################
#Obtaining the Max and Min Values in a Set
basket2={23,45,67,12,456}
print(max(basket2))			#o.p:-456
print(min(basket2))			#o.p:-12

###########################################
#Removing an Item
basket = {'apple', 'orange', 'apple', 'pear', 'orange','banana'}
print(basket)				#o.p:- {'apple', 'pear', 'banana', 'orange'}
basket.remove('apple')			#o.p:- {'banana', 'orange', 'pear'}
basket.discard('apricot')		#o.p:- {'apple', 'pear', 'banana', 'orange'}
print(basket)				#o.p:- {'pear', 'banana', 'orange'}

###########################################
#Set Operations
s1 = {'apple', 'orange', 'banana'}
s2 = {'grapefruit', 'lime', 'banana'}
print('Union:', s1 | s2)			#o.p:- Union: {'orange', 'apple', 'grapefruit', 'banana', 'lime'}
print('Intersection:', s1 & s2)		#o.p:- Intersection: {'banana'}
print('Difference:', s1 - s2)		#o.p:- Difference: {'apple', 'orange'}








































