# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 10:42:07 2024

@author: suraj
"""

# ********************Operation on csv file************************
'''For accesing the file first check the working Directory 
Access the file using the pandas 
Read the content of the file by using the absoulte path and store the data in the file 
#we can perform the operation on the csv file so it is nessaccery that the pandas  libreary are install first
'''
import os
import csv
import pandas as pd
f1 = pd.read_csv('E:/github_Datascience/1_python/buzzers.csv')

######################################################
with open('buzzers.csv')as raw_data:
    print(raw_data.read())
# read () :- read is used to read the file content , it  can read the data as normal form

#####################################################
# reading the CSV Data as lists
with open('buzzers.csv')as raw_data:
    for line in csv.reader(raw_data):
        print(line)
# it can read the file data as in the list form
# [ ]:- data display in square bracket by line by line

####################################################
# reading the CSV data as Dictionaries
with open('buzzers.csv')as raw_data:
    for line in csv.DictReader(raw_data):
        print(line)
# data display in the {} braces becauses of the we use the  dictionary in above and data are read line by lne

####################################################
# another apporach to read the csv data in the dictionaries by using the key value pair
with open('buzzers.csv') as data:
    flights = {}
    for line in data:
        k, v = line.split(",")

        flights[k] = v
flights
# o.p:- it can show the only keys and value in the dictionary form . it having at last in keyword
###########################################################
# stripping then spliting the raw data i.e. /n
with open('buzzers.csv') as data:
    #
    flights = {}
    for line in data:
        k, v = line.strip().split(",")
        flights[k] = v
flights
# o.p:- at the end of the line  each ‘/n’ are present  so that ‘/n’ are split or remove by using the split word
# ***********************************************************
# **Decorator**
# pre_recusittes of the decorator


def plus_one(number):
    number1 = number+1
    return number1


plus_one(5)
# o.p:-6

##############################################
# definigh the function inside the another function


def plus_one(number):

    def add_one(number):
        number1 = number+1
        return number1
    result = add_one(number)
    return result


plus_one(4)
# o.p:-5

#################################################
# passing the argument to the other function


def plus_one(number):
    result1 = number+1
    return result1


def function_call(function):
    result = function(5)
    return result


function_call(plus_one)
# o.p:-6

###############################################

# function retunring the another functions


def hello_function():
    def say_hii():
        return "hii"
    return say_hii


# when you function(say_hii) is returing the function (say_hii)
hello = hello_function()
# then it is nessacary to assign the outer function(hello_function) to the variable(hello)
# And call the varible(hello())
hello()
#o.p:- hii
'''
Note:- always remember when you call the  hello_function() directly then it will display the object not hi
. Therefore you need to assign it to hello first then call hello() function
'''
###################################################
# Pass the function as argument


def add(x, y):
    return x+y


def calculate(func, x, y):
    return func(x, y)


result = calculate(add, 4, 6)
print(result)
# o..p:-10
