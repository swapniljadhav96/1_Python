# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 10:39:40 2024

@author: suraj
"""


"""------------------- assigement day ------------------------"""
# use the admine user
import hashlib
users = ["admine", "employee", "manager", "worker", "staff"]
for user in users:
    if user == "admin":
        print("hello admin ,would you like to see the status report")
    elif user == "employee":
        print("hello employe")
    elif user == "manager":
        print("hello manager")
    elif user == "worker":
        print("hello worker")
    else:
        print("hello staff")

# check the new user and old user
current_user = ["ali", "ahemd", "fahad", "aun", "rana"]
new_users = ["ali", "rana", "bilai", "huzi", "dula"]
for new_user in new_users:
    if new_user in current_user:
        print("person will need to enter  a new uersname")
        break
    else:
        print("saying that the username is avilable")
        break

#####################
# save the password in the form of hash code and check the user password and previous password are correct
hashlib.sha256("Gaurav@1234".encode('utf-8')).hexdigest()
'778d4ce2dfb7063981a67be5ba7955ba063c3319760bd3a0d2a85f5d15a594de'
len(hashlib.sha256("Gaurav@1234".encode('utf-8')).digest())
# 32 bit processor hashlib.sha256

###############
hashlib.sha512("Gaurav@1234".encode('utf-8')).hexdigest()
'778d4ce2dfb7063981a67be5ba7955ba063c3319760bd3a0d2a85f5d15a594de'
len(hashlib.sha512("Gaurav@1234".encode('utf-8')).digest())

# 64 bit processor hashlib.sha512
