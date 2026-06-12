# Mini Project Guess Number

import random

Target=random.randint(1,100)

while True:
    userchoice=int(input("Guess the Target: "))
    if(userchoice==Target):
        print("Success: Correct Guess!!")
    elif (userchoice<Target):
        print("Your number was too small. Take  a Bigger Guess......")
    else:
        print("Your number was too big. Take  a Smaller Guess........")



print("-----------------GAME OVER--------------------")
    