# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 00:08:59 2024

@author: suraj
"""

# **Dictionaries**
'''A Dictionary is a set of associations between a key and a value that is unordered,changeable (mutable) and indexed.
'''
# Operation on the Dictionaries
# 1.Definattion of the Dictionaries
capitals = {
    'Maharashtra': 'Mumbai',
    'Gujrat': 'Ahmadbad',
    'UP': 'Lakhnow',
    'Karnataka': 'Banglore',
    'Andhrapradesh': 'Hydrabad'}
# o.p:- {'Maharashtra': 'Mumbai', 'Gujrat': 'Ahmadbad', 'UP': 'Lakhnow', 'Karnataka': 'Banglore', 'Andhrapradesh': 'Hydrabad'}
print(capitals)

##############################################
# 2.Accessing Items via Keys
# o.p:- capitals[Maharashtra]: Mumbai
print('capitals[Maharashtra]:', capitals['Maharashtra'])

#############################################
# 3.Adding a New Entry
capitals['West_Bengal'] = 'Kolkatta'
capitals
'''#o.p;- {'Maharashtra': 'Mumbai',
 'Gujrat': 'Ahmadbad',
 'UP': 'Lakhnow',
 'Karnataka': 'Banglore',
 'Andhrapradesh': 'Hydrabad',
 'West_Bengal': 'Kolkatta'}
'''
#############################################
# 4.Changing a Keys Value
capitals['Gujrat'] = 'Gandhinagar'
print(capitals)
#o.p:- {'Maharashtra': 'Mumbai', 'Gujrat': 'Gandhinagar', 'UP': 'Lakhnow', 'Karnataka': 'Banglore', 'Andhrapradesh': 'Hydrabad', 'West_Bengal': 'Kolkatta'}

#############################################
# 5.Removing an Entry
capitals.pop('Karnataka')
print(capitals)
#o.p:- {'Maharashtra': 'Mumbai', 'Gujrat': 'Gandhinagar', 'UP': 'Lakhnow', 'Andhrapradesh': 'Hydrabad', 'West_Bengal': 'Kolkatta'}

############################################
# 6.del key word to delete the element by using the key value
del capitals['UP']
print(capitals)
#o.p:- {'Maharashtra': 'Mumbai', 'Gujrat': 'Gandhinagar', 'Andhrapradesh': 'Hydrabad', 'West_Bengal': 'Kolkatta'}

############################################
# 7.Iterating over Keys
capitals = {
    'Maharashtra': 'Mumbai',
    'Gujrat': 'Ahmadbad',
    'UP': 'Lakhnow',
    'Karnataka': 'Banglore',
    'Andhrapradesh': 'Hydrabad'
}
for states in capitals:
    # o.p:- Maharashtra, Gujrat, UP, Karnataka, Andhrapradesh,
    print(states, end=', ')
##########################################

for states in capitals:
    print(states, end=', ')
    print(capitals[states])
'''# o.p:- for states in capitals:
    print(states, end=', ')
    print(capitals[states])
'''
###############################################
# 9.Values, Keys and Items
# o.p:-dict_values(['Mumbai', 'Ahmadbad', 'Lakhnow', 'Banglore', 'Hydrabad'])
print(capitals.values())
# o.p:-dict_keys(['Maharashtra', 'Gujrat', 'UP', 'Karnataka', 'Andhrapradesh'])
print(capitals.keys())
# o.p:- dict_items([('Maharashtra', 'Mumbai'), ('Gujrat', 'Ahmadbad'), ('UP', 'Lakhnow'), ('Karnataka', 'Banglore'), ('Andhrapradesh', 'Hydrabad')])
print(capitals.items())

###############################################
# 10.Checking Key Membership
print('Karnataka' in capitals)  # o.p:- True
print('Bihar' not in capitals)  # o.p: True

#############################################
# 11.Obtaining the Length of a Dictionary
print(len(capitals))  # o.p:- 5

############################################
# 12.Dictionaries can have values in tuple
seasons = {'Summer': ('Feb', 'Mar', 'Apr', 'May'),
           'Rainy': ('June', 'July', 'August', 'Sept'),
           'Winter': ('Oct', 'Nov', 'December', 'January')}
print(seasons['Rainy'])  # o.p:- ('June', 'July', 'August', 'Sept')
print(seasons['Rainy'][1])  # o.p:- July

##########################################
# **Dictionary Methods**
# get() is a useful method to access the values of a key in a dictionary.
print(capitals.get('UP'))  # o.p:- Lakhnow

##########################################
# Duplicates Not Allowed
#Dictionaries cannot have two items with the same key:
dict2 = {
    "brand": "Maruti",
    "model": "Breeza",
    "year": 2021,
    "year": 2020
}
print(dict2)
#o.p:- {'brand': 'Maruti', 'model': 'Breeza', 'year': 2020}

############################################
# Loop Through a Dictionary, it will show only keys
for x in dict2:
    print(x)
#o.p:- brand
model
year

##########################################
# Print all values in the dictionary, one by one:
for x in dict2:
    print(dict2[x])
#o.p:- Maruti
Breeza
2020

#########################################
# You can also use the values() method to return values of a dictionary:
for x in dict2.values():
    print(x)
'''#o.p:- Maruti
Breeza
2020
'''
##########################################
# you can use the keys() method to return the keys of a dictionary:
for x in dict2.keys():
    print(x)
'''#o.p:- brand
model
year
'''
############################################
# Loop through both keys and values, by using the items() method:
for x, y in dict2.items():
    print(x, y)
'''#o.p :-brand Maruti
model Breeza
year 2020
'''
#############################################
# Copy a Dictionary
#Make a copy of a dictionary with the copy() method:
mydict = dict2.copy()
print(mydict)  # o.p:- {'brand': 'Maruti', 'model': 'Breeza', 'year': 2020}

############################

# Write a Python script to add a key to a dictionary.
# Sample Dictionary : {0: 10, 1: 20}
# Expected Result : {0: 10, 1: 20, 2: 30}

d = {0: 10, 1: 20}
print(d)  # o.p:-{0: 10, 1: 20}
d.update({2: 30})
print(d)  # o.p:-{0: 10, 1: 20, 2: 30}

############################################
# adding the value to the dictionary
d = {0: 10, 1: 20}
print(d)  # o.p:-{0: 10, 1: 20}
d[2] = 30  # adding by using index value
print(d)  # o.p:-{0: 10, 1: 20, 2: 30}


###############################################
# Dictionary methods
# clear():Remove all elements from the car list
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
car.clear()
car

#####################################
# copy method
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
x = car.copy()
print(x)

####################
# fromey()
# Create a dictionary with 3 keys, all with the value 0
x = {'key1', 'key2', 'key3'}
y = 0
thisdict = dict.fromkeys(x, y)
thisdict

###############################################################
# pipe operator in the case
match input("Are you sure ? (y/n):"):
case "y":
    print("Done")
case "n":
    print("cancelled")
case cmd:
    print("Unknown command", cmd)
