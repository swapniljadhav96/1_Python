# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 00:50:01 2024

@author: suraj
"""

import json
************************Working with JSON File*********************
# JSON:-Java Script object notation
# Storing the data in the jason file it is important for futur work using the json.dump() and json.load
# Json.dump():- dumps takes an object and produces a string
# Json.load():-  load would take a file _like object read the data from that object and use that string to create an object
number = [2, 3, 4, 5, 6, 74, 34]
file_name = 'number.json'
with open(file_name, 'w') as obj:
    json.dump(number, obj)
# o.p:- the file are created in the working directory
# The nmber are written in the file

######################################################
# saving the data with json file working with user generated  data
username = input("enter the name")
file_name = 'username.json'
with open(file_name, 'w') as obj:
    json.dump(username, obj)
print(f"iwill remmebre you when you come back ,{username}!")
# f:-This is called f string and are quite
# Straight forword :when using on f’ in front of a string all the variable inside curly bracket are read and replaced by there value

#####################################################
# Now lets write new program  that generat user name is alerady has been stored
file_name = 'username.json'
with open(file_name) as obj:
    username = json.load(obj)
print(f"welcome back,{username}!")
# writing the username i.e. '{username}!'
# o.p:- It will rember the preseviosly user name who acess the file

####################################################
# combine two program in one program with the exception handling
# load the username if it has been stored previsoly otherwise promt for the user name and stored it
file_name = 'username.json'
try:
    with open(file_name) as obj:
        username = json.load(obj)
except FileNotFoundError:
    username = input("enter the name")
    file_name = 'username.json'
    with open(file_name, 'w') as obj:
        json.dump(username, obj)
    print(f"iwill remmebre you when you come back ,{username}!")
else:
    print(f" welcome back,{username}!")
