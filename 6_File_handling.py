# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 00:24:18 2024

@author: suraj
"""

#for opening the file first we need to check the working dirtectory
#abstract path:-	'c:/10-python/pi_digits.txt'
#relative path:-	'pi_digits.txt'


with open('pi_digits.txt') as file_object:
    # The open() function needs
    # one argument: the name of the file you want to open.
    contents = file_object.read()
print(contents)
# Observe the extra line at the end of output
#########################
# To avoid this rstrip() method is used
with open('pi_digits.txt') as file_object:
    contents = file_object.read()
print(contents.rstrip())
# rstrip() method removes, or strips, any whitespace
# characters from the right side of a string.
##################################
file_path = 'E:/github_Datascience/1_python/pi_digits.txt'
with open(file_path) as file_object:
    contents = file_object.read()
print(contents.rstrip())
############################
# Reading Line by Line
filename = 'pi_digits.txt'
# we assign the name of the file we’re reading from to the variable
with open(filename) as file_object:
    # We again use the with syntax to
    # let Python open and close
    # the file properly.

    for line in file_object:
        print(line)
##############################
# These blank lines appear because an invisible newline
# character is at the end of each line in the text file.
# Using rstrip() on each line in
# the print() call eliminates these extra blank lines:
filename = 'pi_digits.txt'
with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())
####################################
# Making a List of Lines from a File
# When you use with, the file object returned by open()
# is only available inside
# the with block that contains it.
# If you want to retain access to a file’s contents
# outside the with block,
# you can store the file’s lines in a list
# inside the block and then work with that list.
filename = 'pi_digits.txt'
with open(filename) as file_object:
    lines = file_object.readlines()  # file object is converted to list
# the readlines() method takes each line from the file
# and stores it in a list.
lines
for line in lines:
    print(line.rstrip())
############################################
# Working with a File’s Contents
# After you’ve read a file into memory,
# you can do whatever you want with that data
filename = 'pi_digits.txt'
with open(filename) as file_object:
    lines = file_object.readlines()
    pi_string = ''
    for line in lines:
        pi_string += line.rstrip()
        print(pi_string)
        print(len(pi_string))
###################################
# Writing to a File
# One of the simplest ways to save data is to write it
# to a file. When you write text to a file,
# the output will still be available after
# you close the terminal containing your program’s output.

filename = 'programming.txt'

with open(filename, 'w') as file_object:
    file_object.write("I love programming.")
############################################
# Writing Multiple Lines
# The write() function doesn’t add any newlines
# to the text you write. So if
# you write more than one line without
# including newline characters
filename = 'programming.txt'
with open(filename, 'w') as file_object:
    file_object.write("I love programming.")
    file_object.write("I love creating new games.")
####################################
# Including newlines in your calls to write() makes
# each string appear on its own line

filename = 'programming.txt'
with open(filename, 'w') as file_object:
    file_object.write("I love programming.\n")
    file_object.write("I love creating new games.\n")
#####################################
# Appending to a File
# If you want to add content to a file
# instead of writing over existing content,
# you can open the file in append mode.
# When you open a file in append mode,
# Python doesn’t erase the contents of the file
# before returning the file object.
filename = 'programming.txt'

with open(filename, 'a') as file_object:
    # we use the 'a' argument to open the file for appending
    # rather than writing over the existing file.
    file_object.write("I also love finding meaning in large datasets.\n")
    file_object.write("I love creating apps that can run in a browser.\n")

# another way is that to pass the file name as the input in the open braceses as follows
with open('programming.txt', 'a') as file_object:
    # we use the 'a' argument to open the file for appending
    # rather than writing over the existing file.
    file_object.write("I also love finding meaning in large datasets.\n")
    file_object.write("I love creating apps that can run in a browser.\n")
