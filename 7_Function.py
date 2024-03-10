# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 00:31:32 2024

@author: suraj
"""

# When you are writing a program
# if you find yourself writing the same code
# more than once, it is probably best to
# define a function with the repeated code
# in it.

# passing the num as the default function
from pizza import *
import pizza as p
from pizza import make_pizza as mp
from pizza import make_pizza
import pizza


def prime_num(num):
    for i in range(2, num):
        if (num % i == 0):
            return "The number is not prime"
            break

    return "The number is prime"


print(prime_num(12))


# arbitary function -> passing the num as the arbitary function
num = int(input('enter the number:-'))


def prime_num():
    for i in range(2, num):
        if (num % i == 0):
            return "The number is not prime"
            break

    return "The number is prime"


print(prime_num())

########################


def greet_user():
    #"""Display a simple greeting."""
    print("Hello!")


greet_user()

# Passing Information to a Function


def greet_user(username):
    # Display a simple greeting."""
    print(f"Hello, {username}!")


greet_user('Sanjivani AI')
############
#Arguments and Parameters
# The variable username in the def of greet_user() is an example of a


def describe_pet(animal_type, pet_name):
    # Display information about a pet.
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name}.")


describe_pet('Dog', 'Moti')
# Order Matters in Positional Arguments

describe_pet('Moti', 'Dog')
# Default Values
# When writing a function, you can define a default value for each parameter.


def describe_pet(pet_name, animal_type='dog'):
    # Display information about a pet.
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")


describe_pet(pet_name='Moti')
##################################
# Avoiding Argument Errors


def describe_pet(animal_type, pet_name):
    # Display information about a pet.
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")


describe_pet()
##########################
# Return Values


def get_formatted_name(first_name, last_name):
    # Return a full name, neatly formatted.
    full_name = f"{first_name} {last_name}"
    return full_name


musician = get_formatted_name('Ram', 'Sarkar')
print(musician)
###########################
# Returning a Dictionary


def build_person(first_name, last_name):
    # Return a dictionary of information about a person."""
    person = {'first': first_name, 'last': last_name}
    return person


musician = build_person('Ram', 'Sarkar')
print(musician)
###########################
# Passing a List
# You’ll often find it useful to pass a list to a function, whether it’s a list of
# names, numbers, or more complex objects,
# such as dictionaries.


def greet_users(names):
    # Print a simple greeting to each user in the list."""
    for name in names:
        msg = f"Hello, {name.title()}!"
        print(msg)


usernames = ['Sanket', 'Saurabh', 'Surabhi']
greet_users(usernames)
#################################
# Passing an Arbitrary Number of Arguments


def make_pizza(*toppings):
    # Print the list of toppings that have been requested."""
    print(toppings)


make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')
# Now we can replace the print() call with a loop that runs through the
# list of toppings and describes the pizza being ordered:


def make_pizza(*toppings):
    # Summarize the pizza we are about to make."""
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")


make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')
###############################
# Mixing Positional and Arbitrary Arguments


def make_pizza(size, *toppings):
    # Summarize the pizza we are about to make."""
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")


make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
################################

pizza.make_pizza(16, 'pepperoni')
pizza.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
############################
# importing Specific Functions
make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
# Using as to Give a FunctionS an Alias
mp(16, 'pepperoni')
mp(12, 'mushrooms', 'green peppers', 'extra cheese')
###########################
# Using as to Give a Module an Alias
p.make_pizza(16, 'pepperoni')
p.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
####################################
# Importing All Functions in a Module
make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# scope of variable
x = x+1
x = 6
print(x)
# You cannot reference a variable
# until it has been assigned a value.
