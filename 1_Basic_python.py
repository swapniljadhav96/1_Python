# -*- coding: utf-8 -*-
"""
Created on Sat Mar  9 22:56:59 2024

@author: suraj
"""

'''1. Download the Anaconda Installer:
a.Visit the Anaconda website.
b.Under "Individual," choose the Python 3.x version.
c.Download the Windows 64-bit installer.

2. Install Anaconda:
a.Double-click the downloaded installer (.exe file).
b.Important: During installation, ensure you check the box to "Add Anaconda to your PATH environment variable." This allows you to run Anaconda tools from any command prompt window.
c.Follow the on-screen instructions to complete the installation.

3. Verify Installation:
a.Open a Command Prompt window: Press the Windows key, type "cmd," and press Enter.
b.Type conda --version and press Enter. If successful, you'll see the installed conda version.
c.To check if Spyder is also installed (it often is with Anaconda), type spyder --version and press Enter. You should see the installed Spyder version (if it was included).

4. Launch Anaconda Navigator:
a.Find Anaconda Navigator in your Start menu and launch it.
This gives you a graphical interface to manage Anaconda environments and packages.

5. Launch Spyder (Optional):
You can also launch Spyder directly from the Command Prompt window by typing spyder and pressing Enter. Spyder is an IDE specifically designed for scientific computing in Python.
That's it! You've successfully install'''

#from the input() function into an int. We can do this by wrapping the call to the input() function in a call
# print Hello World

print('Hello World')
#O/p: - Hello word

''' .py extension. Such a file can contain one or more Python statements that represent a Python
program or Script.
Note: Please note that Python for its scope doesn’t depend on the braces ( { } ), instead it uses
indentation for its scope
In the python2 the ‘print’ is not the function  but a keyword and therefore can be used without
parentheses In python 3  the “print” is the function and must be involked with paraentheses
 '''
# ********************************************************************************************************
# **Variable's**
'''#Variables are containers for storing data values.
# Creating Variables:-Python has no command for declaring a variable. A variable is created the moment
you first assign a value to it.
# Types of Numbers-There are three types used to represent numbers in Python; these are integers (or
integral) types, floating point numbers and complex numbers. '''

x = 1
print(x)    # o/p:-1
print(type(x))    # o/p:- integer
######################
x = 100000000000000000000000000000000000000000000000000000000001
print(x)
 # o/p:100000000000000000000000000000000000000000000000000000000001
print(type(x))  # o/p:- integer
'''
This makes it very easy to work with integer numbers in Python. Unlike some programming languages
such as C# and Java have different integer types depending on the size of the number, small numbers
having to be converted into larger types in some situations.
'''
##################
# Example
x = 5
y = "John"
print(x)  # o/p:-5
print(y)  # o/p:-John
######################
# Variables do not need to be declared with any particular type, and can even change type after they have been set.
#example
x = 4  # x is of type int
x = "Sally"  # x is now of type str
print(x)  # o/p:-Sally
#******************************************************************************
#**Casting**
#If you want to specify the data type of a variable, this can be done with casting.
#Example
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0
#******************************************************************************
#**Get the Type**
#You can get the data type of a variable with the type() function.
#Example
x = 5
y = "John"
print(type(x))  # o/p:-integer
print(type(y))  # o/p:-string
#*******************************************************************************
#**Single or Double Quotes?**
#String variables can be declared either by using single or double quotes:
#Example
x = "John"  # is the same as
x = 'John'
#*******************************************************************************
#**Case-Sensitive**
#Variable names are case-sensitive.
#Example
#This will create two variables:
a = 4
A = "Sally"  # A will not overwrite a
#*******************************************************************************
#**Variable Names**
'''A variable can have a short name(like x and y) or a more descriptive name(age, carname,
total_volume).
 Rules for Python variables:
✓ A variable name must start with a letter or the underscore character
✓ A variable name cannot start with a number
✓ A variable name can only contain alpha-numeric characters and underscores(A-z, 0-9, and _)
✓ Variable names are case-sensitive(age, Age and AGE are three different variables)
✓ A variable name cannot be any of the Python keywords.
'''
#Example
#Legal variable names:
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

####################
#Example
#Illegal variable names:
2myvar = "John"
my-var = "John"
my var = "John"
#Remember that variable names are case-sensitive
#######################
#**Multi Words Variable Names**
#Variable names with more than one word can be difficult to read.
#There are several techniques you can use to make them more readable:

#Camel Case
#Each word, except the first, starts with a capital letter:
myVariableName = "John"

#Pascal Case
#Each word starts with a capital letter:
MyVariableName = "John"

#Snake Case
#Each word is separated by an underscore character:
my_variable_name = "John"

#Many Values to Multiple Variables
#Python allows you to assign values to multiple variables in one line:
E#xample
x, y, z = "Orange", "Banana", "Cherry"
print(x)  # o/p:- Orange
print(y)  # o/p:-Banana
print(z)  # o/p:- Cherry

#Note: Make sure the number of variables matches the number of values, or else you will get an error.

#One Value to Multiple Variables
#And you can assign the same value to multiple variables in one line:
#Example
x = y = z = "Orange"
print(x)  # o/p:-Orange
print(y)  # o/p:-Orange
print(z)  # o/p:-Orange

#Unpack a Collection
#If you have a collection of values in a list, tuple etc. Python allows you to extract the values into variables. This is called unpacking.
#Example
#Unpack a list:
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)  # o/p:-apple
print(y)  # o/p:-banana
print(z)  # o/p:-cherry

#Output Variables
#The Python print() function is often used to output variables.
#Example
x = "Python is awesome"
print(x)  # o/p:- Python is awesome

#In the print() function, you output multiple variables, separated by a comma:
#Example
x = "Python"
y = "is"
z = "awesome"
print(x, y, z)  # o/p:-Python,is, awesome

#You can also use the + operator to output multiple variables:
#Example
x = "Python "
y = "is "
z = "awesome"
print(x + y + z)  # o/p:- Pythonisawesome
#Notice the space character after "Python " and "is ", without them the result would be
#"Pythonisawesome".

##################################################
#For numbers, the + character works as a mathematical operator:
#Example
x = 5
y = 10
print(x + y)  # o/p:-15

###################################################
#In the print() function, when you try to combine a string and a number with the + operator, Python will
#give you an error:
#Example
x = 5
y = "John"
print(x + y)  # o/p:-error

#The best way to output multiple variables in the print() function is to separate them with commas,
#which even support different data types:
#Example
x = 5
y = "John"
print(x, y)  # o/p:-5 John

#*******************************************************
#**Global Variables**
'''Variables that are created outside of a function(as in all of the examples above) are known as global
variables. Global variables can be used by everyone, both inside of functions and outside.
'''
#Example
#Create a variable outside of a function, and use it inside the function
x = "awesome"
def myfunc():
  print("Python is " + x)

myfunc()  # o/p:- Python is awesome
###################################
'''If you create a variable with the same name inside a function, this variable will be local, and can only
be used inside the function. The global variable with the same name will remain as it was, global and
with the original value.'''
#Example
#Create a variable inside a function, with the same name as the global variable
x = "awesome"  # golable declare
def myfunc():  # function create
   x = "fantastic"
   print("Python is " + x)
   
myfunc()
print("Python is " + x)
######################################
# **Converting to Ints**
'''It is possible to convert another type into an integer using the int() function. For example, if we want to
convert a string into an int(assuming the string contains a integer number) then we can do this using
the int() function.
'''
#For example
total = int('100')
'''This can be useful when used with the input() function. The input() function always returns a string. If
we want to ask the user to input   an integer number, then we will need  to convert the string returned
to the int() function.'''
#Example
age = input('Please enter your age:')
print(type(age))  # o/p:-string
print(age)  # o/p:- user need

########################################
#example
age1 = input('Please enter your age:')
print(type(age1))  # o.p:- string
print(age1)  # o.p:- user need

########################################
#example
age2 = input('Please enter your age:')
print(type(age2))  # o.p:- string

print(age2)  # o.p:- as per user need
age = age1+age2  # o.p:- the two string are concatenated
print(age)  # o.p:- 2 concatenated string

########################################
#example
age = int(input('Please enter your age:'))
print(type(age))  # o.p:- int
print(age)  # o.p:-- as per user need

########################################
#example
age1 = int(input('Please enter your age:'))
print(type(age1))  # o.p:- int
print(age1)  # o.p:- as per user need

########################################
#example
age2 = int(input('Please enter your age:'))
print(type(age2))  # o.p:-int
print(age2)  # o.p:- as per user need
age = age1+age2  # o.p:- 2 integer value are added
print(age)     # o.p:- total of the age1and age2

########################################
#**Floating Point Numbers**
'''Real numbers, or floating point numbers, are represented in Python using the IEEE 754 double
precision binary floating-point number format'''

#Example
exchange_rate = 1.83
print(exchange_rate)  # o.p:- 1.83
print(type(exchange_rate))  # o.p:- float

#**Converting to Floats**
#As with integers it is possible to convert other types such as an int or a string into a float.
#Example
int_value = 100
string_value = '1.5'
# here the integer value are converted into the float
float_value = float(int_value)
print('int value as a float:', float_value)  # o.p:- 100.00
print(type(float_value))  # o.p  :- float
# here the string is converted into the float
float_value = float(string_value)
print('string value as a float:', float_value)  # o.p:-1.5
print(type(float_value))  # o.p:- float
#******************************************************************************
#Complex Numbers
c1 = 1
c2 = 2j
print('c1:', c1, ', c2:', c2)  # o.p:- c1:-1;c2:-2j
print(type(c1))  # o.p:-real
print(type(c2))  # o.p:-imagenery
print(c1.real)  # print  the real part i.e 1
print(c2.imag)  # print the imaginary part 2j
#*********************************************************************************
#Boolean Values
#Python supports another type called Boolean; a Boolean type can only be one of True or False
#Example
all_ok = True
print(all_ok)  # O.p:- True
all_ok = False
print(all_ok)  # o.p:- False
print(type(all_ok))  # o.p:-Boolean

###############################################
# You can also convert strings into Booleans as long as the strings contain either True or False (and nothing else).
status=bool(input('OK it is confirmed: '))
print(status)  # o.p:- true
print(type(status))  # o.p:- true
#***********************************************************************************
#**Arithmetic Operators**
'''Arithmetic operators are used to perform some form of mathematical operation such as addition,
subtraction, multiplication and division etc. In Python they are represented by one or two characters.'''
#Example
home=10
away=15
print(home + away)  # o.p:- 1015
print(type(home + away))  # o.p:- string
print(10 * 4)  # o.p:- 40
print(type(10*4))  # o.p:- int
goals_for=10
goals_against=7
print(goals_for - goals_against)  # o.p:- 3
print(type(goals_for - goals_against))  # o.p:- int

###########################################
'''However, you may notice that we have missed out division with respect to integers, why is this? It is
because it depends on which division operator you use as to what the returned type actually is .
For example, if we divide the integer 100 by 20 then the result you might reasonably expect to produce
might be 5; but it is not, it is actually 5.0:'''
#Example
print(100 / 20)  # o.p;- 5
print(type(100 / 20))  # o.p:- int
##########################################
'''To ignore the fractional part then there is an alternative version of the divide operator // . This operator
is referred to as the integer division operator'''
#Example
print(100 // 20)  # o.p:- 5.0
print(type(100 // 20))  # o.p:- float

###########################################
'''But what if you are only interested in the remainder part of a division, the integer division operator has
lost that? Well in that case you can use the modulus operation %'''
#Example
print('Modulus division 100 % 13:', 100 % 13)  # o.p:- 9
print('Modulus division 3 % 2:', 3 % 2)  # o.p:- 1

##########################################
#A final integer operator we will look at is the power operator that can be used to raise an integer by a
#given power,
#for example
#5 to the power of 3.
#The power operator is '**'
a=5
b=3
print(a ** b)  # o.p:- 125
#**********************************************************************************
#**Assignment Operators**
'''These assignment operators are actually referred to as compound operators as they combine together
a numeric operation(such as add) with the assignment operator.
 For example, the += compound operator is a combination of the add operator and the=operator'''
#example
x=0
x += 1  # has the same behaviour as x = x + 1
#****************************************************************************************
#**None Value**
#Python has a special type, the None Type, with a single value, None.
#Example
winner=None
print(winner is None)  # o.p:- True
# Alternatively you can also write:
print(winner is not None)  # o.p:-False

# Which will print out True only if the
winner=None
print('winner:', winner)  # o.p:- winner: None
print('winner is None:', winner is None)  # o.p:- winner is None: True
# o.p:- winner is not None: False
print('winner is not None:', winner is not None)
print(type(winner))  # o.p:- <class 'NoneType'>
print('Set winner to True')  # o.p:- Set winner to True
winner=True
