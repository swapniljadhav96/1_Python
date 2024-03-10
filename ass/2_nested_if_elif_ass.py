'''
Write python code using  if elif.so as to check height as well as
so as to allow for roller coster,using elif further you check
age category and charge ticket accordingly
@author:Radhakrishna
'''

print("Welcome to the roller coaster")
height=int(input("Please enter your height"))

if height>=120:
    print("you can ride the roller coaster")
    age=int(input("Please enter your age "))
    if age<12:
        print("your ticket will be 5$")
    elif age>12 and age<18:
        print("your ticket will be 7$")

    elif age>18:
        print("your ticket will be 12$")
else:
    print("Sorry,you need to grow taller before you can ride")    