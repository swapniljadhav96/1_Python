# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 00:56:30 2024

@author: suraj
"""

#Assigment day
# adjectives= name of adjective
# noun=name of the noun
# password=join the all strig
import string
adjectives=['sleepy', 'slow', 'smelly', 'wet',
    'fat', 'red', 'orange']  # pick the adjectives
noun=['apple', 'dinosor', 'ball', 'toaster', 'goat',
    'dragon', 'hammer', 'dduck', 'panda']  # pick the noun
import random  # pick the words randomly
adjectives=random.choice(adjectives)
noun=random.choice(noun)
number=random.randrange(0, 100)  # selcte the number
special_char=random.choice(string.punctuation)  # sleect the special character
# create the new secure password
password=adjectives+noun+str(number)+special_char
print('your new password is:-%s' % password)
# %s:-
print(f'your new password is:- {password}')

####################################################
# another  way is also to generate the password u can use the while loop also and if condition
# responce=taking the input from the user in the below program it can give the another password also if you are not statistified with  inlial one
print("wlecome back to password picker")
while True:
    adjectives=random.choice(adjectives)
    noun=random.choice(noun)
    number=random.randrange(0, 100)
    special_char=random.choice(string.punctuation)
    password=adjectives+noun+str(number)+special_char
    print(f'your new password is:-{password}')
    responce=input('would you want too enter the new password type y or n:-')
    if responce == 'n':
        break
   # else:
    #    continue

##########################################################
# take input from user for password and check for the generated password is good or bad
noun=[]
adj=[]
import string
import random
while True:
    n=input(' enter the list of the noun with start with the  capital letter :-')
    noun.append(n)
    a=input(" enter the list of the adjectives with start with the capital letter:-")
    adj.append(a)
    responce=input(
        'would you want too append the list ao adj or noun (type y or n):-')
    if responce == 'n':
        break
print(noun)
print(adj)
adj=random.choice(adj)
noun=random.choice(noun)
number=random.randrange(0, 100)
special_char=random.choice(string.punctuation)
password=adj+noun+str(number)+special_char
print(f'your new password is:-{password}')
def pass_word(password):  # defining the function
     for x in password:
         if x >= "A" and x <= "Z":
             has_upper=True
         elif x >= "a" and x <= "z":
             has_lower=True
         elif x >= "0" and x <= "9":
             has_num=True
     if len(password) >= 8 and has_upper and has_lower and has_num:
         return True
     else:
         return False
# t= input("enter the password:-")
if pass_word(password):        # checkpassword:-is the function that can check the password
     print("Good password")
else:
     print("Bad password")
