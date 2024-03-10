print("Welcome to the pizza hut")
size_pizza=input("please enter the size of pizza,S,M,L:")
add_pepp=input("do you want pepproni ?Y or N: ")
extra_cheese=input("do you want extra Cheese,Y or N:")
bill=0
if size_pizza=='S':
    print("You need to pay $ 15")
    bill=15
elif size_pizza=='M':
    print("You need to pay $20")
    bill=20
elif size_pizza=='L':
    print("You need to pay $ 25")
    bill=25
if add_pepp=='Y':
    if size_pizza=='S':
        bill+=2
    else:
        bill+=3
if extra_cheese=='Y':
    bill+=1
    print(f"You need to pay total bill in ${bill}")
else:
    print(f"you need to pay total bill in ${bill}")

