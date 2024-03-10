# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 00:17:33 2024

@author: suraj
"""

##############################################
'''Write a Python script to concatenate the following dictionaries to create a new one.
Sample Dictionary :
    '''
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
#Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
'''
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
dic4 = {}
for d in (dic1, dic2, dic3): dic4.update(d)
print(dic4)         #o.p:-{1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
'''
################################################
#Write a Python script to check whether a given key already exists in a dictionary. 
d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
def is_key_present(x):
  if x in d:
      print('Key is present in the dictionary')
  else:
      print('Key is not present in the dictionary')
is_key_present(5)
is_key_present(9)
#o.p:-Key is present in the dictionary
#o.p:-Key is not present in the dictionary

###################################################
#Write a Python program to iterate over dictionaries using for loops. 
d = {'x': 10, 'y': 20, 'z': 30} 
for dict_key, dict_value in d.items():
    print(dict_key,':',dict_value)
'''#o.p:-x : 10
y : 20
z : 30'''

#####################################################
'''Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x).
Sample Dictionary ( n = 5) :
Expected Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}'''
n=int(input("Input a number "))
d = dict()
for x in range(1,n+1):
    d[x]=x*x
print(d) #o.p:-Input a number 5
#o.p:-{1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

###############################################
#Write a Python script to merge two Python dictionaries. 
def merge_dictionaries(*dicts):
  result = dict()
  for d in dicts:
    result.update(d)
  return result
#Let us define first dictionory
students1 = {
  'Theodore': 10,
  'Mathew': 11,
}
#The second dictionory
students2 = {
  'Roxanne': 9
}
print("Original dictionaries:")
print(students1)
print(students2)
print("\nMerge dictionaries:")
print(merge_dictionaries(students1, students2))
'''o.p:-Original dictionaries:{'Theodore': 10, 'Mathew': 11}{'Roxanne': 9}
Merge dictionaries:{'Theodore': 10, 'Mathew': 11, 'Roxanne': 9}'''

################################################
#Write a Python program to sum all the items in a dictionary. 
my_dict = {'data1':100,'data2':-54,'data3':247}
print(sum(my_dict.values()))        #o.p:-293

################################################
#Write a Python program to multiply all the items in a dictionary.
my_dict = {'data1':100,'data2':-54,'data3':247}
result=1
for key in my_dict:    
    result=result * my_dict[key]
print(result)       #o.p:--1333800

############################
#Write a Python program to remove a key from a dictionary.
myDict = {'a':1,'b':2,'c':3,'d':4}
print(myDict)
if 'a' in myDict: 
    del myDict['a']
print(myDict)
'''o.p:-{'a': 1, 'b': 2, 'c': 3, 'd': 4}
{'b': 2, 'c': 3, 'd': 4}'''

#############################################
#Write a Python program to map two lists into a dictionary. 
keys = ['red', 'green', 'blue']
values = ['#FF0000','#008000', '#0000FF']
color_dictionary = dict(zip(keys, values))
print(color_dictionary)
'''o.p:-{'red': '#FF0000', 'green': '#008000', 'blue': '#0000FF'}'''

############################################
#Write a Python program to sort a given dictionary by key. 
color_dict = {'red':'#FF0000',
          'green':'#008000',
          'black':'#000000',
          'white':'#FFFFFF'}

for key in sorted(color_dict):
    print("%s: %s" % (key, color_dict[key]))
'''o.p:-black: #000000
green: #008000
red: #FF0000
white: #FFFFFF'''

##############################################
#Write a Python program to get the maximum and minimum values of a dictionary.
my_dict = {'x':500, 'y':5874, 'z': 560}
key_max = max(my_dict.keys(), key=(lambda k: my_dict[k]))
key_min = min(my_dict.keys(), key=(lambda k: my_dict[k]))
print('Maximum Value: ',my_dict[key_max])       #o.p:-Maximum Value:  5874
print('Minimum Value: ',my_dict[key_min])       #o.p:-Minimum Value:  500

###############################################
#Write a Python program to print all distinct values in a dictionary.
L = [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
print("Original List: ",L)
u_value = set( val for dic in L for val in dic.values())
print("Unique Values: ",u_value)
'''o.p:-Original List:  [{'V': 'S001'}, {'V': 'S002'}, {'VI': 'S001'}, {'VI': 'S005'}, {'VII': 'S005'}, {'V': 'S009'}, {'VIII': 'S007'}]
Unique Values:  {'S005', 'S007', 'S001', 'S009', 'S002'}'''

###############################################
#Write a Python program to find the highest 3 values of corresponding keys in a dictionary. 
from heapq import nlargest
my_dict = {'a':500, 'b':5874, 'c': 560,'d':400, 'e':5874, 'f': 20}  
three_largest = nlargest(3, my_dict, key=my_dict.get)
print(three_largest) 
#o.p:-['b', 'e', 'c']

#warmup question
#revere the word
def reverse_words(input):
    if input=="":
        return "You have entered wrong input"
    else:
        words=input.split()
        reverse_sentence="  ".join(reversed(words))
    return reverse_sentence
print(reverse_words("This is India"))

#another way
def reverse(input):
    if input=="":
       return "you have entered wrong input"
    else:
        string=input[::-1]
    return string
print(reverse("This"))

###########################################
#value found in the list or not
lst=[10,20,30,700,80,45]
def search(lst,value):
    for i in range(len(lst)):
        if lst[i]==value:
           return "The value has been found at position  {}".format(i)
    return " Value not found"  
print(search(lst,12))   
#o.p:- Value not found

##################################################
#write python code to find fibbonacy series
def fibbo(n):
        lst=[]
        previous=0
        current=1
        lst.append(current)
        for i in range(n-1):
            previous,current=current,previous+current 
            lst.append(current)
        return lst    
print(fibbo(8))

###########################################################
def fibbo(n):
    lst=[]
    previous=0
    current=1
    lst.append(current)
    for i in range(n-1):
        previous,current=current,previous+current
        lst.append(current)
    return lst    
print(fibbo(8))
###########################################################
cities=["Mumbai","New york","Paris"]
countries=["India","USA","France"]
z=zip(cities,countries)
z
for i in z:
    print(i)
d={city:country for city,country in zip(cities,countries)}
print(d)
#Write a program  that takes a string and return the number of vowels regardless of case sensitivity
def count_vovwels(input):
    #initialize the counter
    count=0
    #for letter in input
    for i in range(len (input)):
        #get the character from input and convert to lower case
        choice=input[i]
        current=choice.lower()
        #current=input.lower()[i]
        if(current=='a' or current=='e' or current=='i' or current=='o' or current=='u'):
            count=count+1
    return count 
print(count_vovwels('AEIOU'))       